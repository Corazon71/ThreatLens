---

# ThreatLens - End-to-End MLOps Pipeline for Phishing URL Detection

ThreatLens is a modular and scalable system designed to detect phishing URLs. It leverages an **end-to-end MLOps pipeline**, enabling automation across the entire machine learning lifecycle. The project integrates **GitHub Actions**, **Docker**, and **AWS services** for CI/CD/CD, ensuring seamless deployment in production environments.

---

## Key Features

- **End-to-End Automation**:
  - Fully automated pipelines for data processing, model training, and deployment.
- **Modular Architecture**:
  - Independent modules for each stage to enhance scalability and maintainability.
- **Cloud-Native Deployment**:
  - Deployed using **AWS EC2** and containerized with **Docker**.
- **Robust Validation**:
  - Schema-based data validation to ensure data quality.
- **Model Performance**:
  - Optimized phishing URL detection using the **XGBoost Classifier**.

---

## Folder Structure

Here is the high-level organization of the project:

```plaintext
ThreatLens/
├── .github/workflows/       # GitHub Actions workflows for CI/CD pipelines
├── Airflow/dags/            # Airflow DAGs for orchestrating tasks
├── Artifacts/               # Stores intermediate files and final model artifacts
├── Data/                    # Raw data and prepared datasets
├── Data_Schema/             # Schema definitions for data validation
├── Notebook/                # Jupyter Notebooks for exploratory data analysis
├── Saved_Models/            # Trained models saved in serialized format
├── Templates/               # HTML templates or configurations for the app
├── Threat_Lens/             # Core Python package with project logic
├── logs/                    # Logging files for debugging and monitoring
├── Dockerfile               # Dockerfile to containerize the application
├── LICENSE                  # License information
├── README.md                # Documentation for the project
├── Requirements.txt         # List of Python dependencies
├── Start.sh                 # Shell script to initialize the project
├── Start_Training.py        # Entry point for the training pipeline
├── docker-compose.yaml      # Docker Compose configuration for local testing
├── get_data.py              # Script for data ingestion
├── main.py                  # Main application entry point
├── setup.py                 # Installation script for the Python package
```

---

## Pipeline Workflow

### 1. **Data Ingestion**
- **Source**: Dataset from Kaggle.
- **Storage**: Uploaded to MongoDB.
- **Output**: Train/test split data saved as artifacts.

### 2. **Data Validation**
- **Schema-based Validation**: Ensures data integrity by verifying schema compliance.
- Detects missing or invalid data entries early.

### 3. **Data Transformation**
- **Preprocessing**:
  - Handles missing values.
  - Converts categorical data to numerical formats.
- Produces clean datasets for training.

### 4. **Model Training**
- **Algorithm**: XGBoost Classifier for phishing URL detection.
- **Output**: Serialized `.pkl` model saved in the `Saved_Models/` directory.

### 5. **Model Evaluation**
- Evaluates performance using:
  - **Accuracy**, **Precision**, **Recall**, and **F1-Score**.
- Selects the best-performing model for deployment.

### 6. **Model Pusher**
- Saves the final trained model in the `Artifacts/` directory for deployment.

### 7. **Deployment**
- **Dockerized Pipeline**:
  - Docker images built and stored in AWS Elastic Container Registry (ECR).
- **AWS EC2 Hosting**:
  - Automated deployment ensures updates with every code push.

---

## Installation and Usage

### Prerequisites
- **Python 3.8+**
- **Docker** installed locally.
- **AWS CLI** configured with appropriate credentials.
- **MongoDB** for data storage.

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Corazon71/ThreatLens.git
   cd ThreatLens
   ```

2. Install dependencies:
   ```bash
   pip install -r Requirements.txt
   ```

3. Run the pipeline:
   ```bash
   python Start_Training.py
   ```

4. Deploy locally using Docker:
   ```bash
   docker-compose up --build
   ```

---

## Deployment Pipeline

This project employs an automated CI/CD/CD workflow managed via **GitHub Actions**:

1. **Continuous Integration (CI)**:
   - Linting, testing, and Docker image creation.
2. **Continuous Delivery (CD)**:
   - Pushes Docker images to AWS Elastic Container Registry (ECR).
3. **Continuous Deployment (CD)**:
   - Deploys the image on AWS EC2, ensuring a live service.

---
