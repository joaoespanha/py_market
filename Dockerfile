FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


#CMD [ "python3", "py_market/mydb.py" ]   

#ENTRYPOINT [ "python3", "py_market/manage.py", "migrate" ]


CMD [ "python3", "py_market/manage.py"  , "runserver", "0.0.0.0:8000" ]