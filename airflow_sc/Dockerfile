FROM apache/airflow:latest

COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt