FROM python:alpine3.16 

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

# CMD [ "python3", "-m", "flask", "--app", "./main", "run", "--host=0.0.0.0" ]
CMD [ "waitress-serve", "main:app" ]