import os

class S3Sync:
  def Sync_Fldr_2_S3(self, Fldr, AWS_Bucket_URL):
    cmnd = f"aws s3 sync {Fldr} {AWS_Bucket_URL}"
    os.system(cmnd)
  
  def Sync_Fldr_from_S3(self, Fldr, AWS_Bucket_URL):
    cmnd = f"aws s3 sync {AWS_Bucket_URL} {Fldr}"
    os.system(cmnd)