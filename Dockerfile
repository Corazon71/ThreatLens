# Use Python 3.11-slim-buster as the base image
FROM python:3.11-slim-buster

# Use root user for permissions
USER root

# Create a directory for your application
RUN mkdir /App

# Copy the current directory contents into the container at /app
COPY . /App/

# Set the working directory to /app
WORKDIR /App/

# Install the required Python packages
RUN pip3 install -r Requirements.txt

# Set Airflow environment variables
ENV AIRFLOW_HOME="/App/Airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True

# Set the correct absolute path for the SQLite database
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////App/Airflow/airflow.db

# Initialize the Airflow database
RUN airflow db init

# Create an Airflow admin user
RUN airflow users create -e gurunaths6102003@gmail.com -f Gurunath -l Salve -p Shambres -r Admin -u Trafalgar

# Set permissions for the start script
RUN chmod 777 Start.sh

# Update the package manager
RUN apt update -y

# Define the entrypoint and command to start the Airflow service
ENTRYPOINT [ "/bin/sh" ]
CMD ["Start.sh"]
