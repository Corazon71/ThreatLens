FROM python:3.11-slim-buster
USER root
RUN mkdir /App
COPY . /App/
WORKDIR /App/
RUN pip3 install -r Requirements.txt
ENV AIRFLOW_HOME = "/App/Airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT = 1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING = True
RUN airflow db init
RUN airflow users create -e gurunaths6102003@gmail.com -f Gurunath -l Salve -p Shambres -r Admin -u Trafalgar
RUN chmod 777 Start.sh
RUN apt update -y
ENTRYPOINT [ "/bin/sh" ]
CMD [ "Start.sh" ]