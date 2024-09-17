import os
import sys

import pymongo
import certifi

import pandas as pd

from dotenv import load_dotenv

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

from Threat_Lens.Constants.Training_Pipeline import DATA_INGESTION_COLLECTION_NAME
from Threat_Lens.Constants.Training_Pipeline import DATA_INGESTION_DATABASE_NAME
from Threat_Lens.Constants.Training_Pipeline import SAVED_MODEL_DIR
from Threat_Lens.Utils.Main_Utils.Utils import Load_object
from Threat_Lens.Utils.ML_Utils.Model.Estimator import ModelResolver
from Threat_Lens.Pipeline.Training_Pipeline import TLTrainingPipeline

from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates

from starlette.responses import RedirectResponse

from uvicorn import run as AppRun

load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL")
CA = certifi.where()

Client = pymongo.MongoClient(MONGODB_URL)
Database = Client[DATA_INGESTION_DATABASE_NAME]
Collection = Client[DATA_INGESTION_COLLECTION_NAME]

Templates = Jinja2Templates(directory = "./Templates")

App = FastAPI()
origins = ["*"]

App.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ["*"]
)

@App.get("/", tags = ["authentication"])
async def Idx():
  return RedirectResponse(url = "/docs")

@App.get("/train")
async def TrainRoute():
  try:
    TrainPL = TLTrainingPipeline()
    if TrainPL.IS_PL_Rnng:
      return Response("Training Pipeline is running already !!")
    TrainPL.Run_Pipeline()
    return Response("Training Successful !!")
  except Exception as e:
    raise TLException(e, sys)
  
@App.post("/predict")
async def PredictRoute(request : Request, file : UploadFile = File(...)):
  try:
    DF = pd.read_csv(file.file)
    Model = ModelResolver(Model_Dir = SAVED_MODEL_DIR)
    Latest_ModelPath = Model.get_best_model_path()
    Latest_Model = Load_object(Latest_ModelPath)
    yPred = Latest_Model.predict(DF)
    DF['PredictedColumn'] = yPred
    DF['PredictedColumn'].replace(-1, 0)

    TableHTML = DF.to_html(classes = 'table table-striped')
    return Templates.TemplateResponse("Table.html", {"request" : request, "table" : TableHTML})
  except Exception as e:
    raise TLException(e, sys)
  
if __name__ == "__main__":
  AppRun(App, host = "localhost", port = 8000)