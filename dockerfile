FROM python:3.10.12
WORKDIR /usr/src/app/meliuztest
COPY /apimeliuz .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["cd", "apimeliuz"]
CMD ["coverage", "run", "--source='.'", "manage.py", "test"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]