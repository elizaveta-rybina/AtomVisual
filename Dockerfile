FROM python:3.10
WORKDIR /usr/src/app
RUN pip install --upgrade pip

COPY . ./
RUN pip install -r enviroment/requirements.txt

EXPOSE 8080
CMD ["python", "app.py"]