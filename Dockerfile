FROM python:3.6.6-slim

#VOLUME ./:app/

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

# ENTRYPOINT python flask_api.py 4000
CMD ["python", "flask_api.py"]
