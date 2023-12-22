FROM python:3.10-alpine3.19 

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8080
# CMD [ "python3", "-m", "flask", "--app", "./main", "run", "--host=0.0.0.0" ]
CMD [ "waitress-serve", "main:app" ]