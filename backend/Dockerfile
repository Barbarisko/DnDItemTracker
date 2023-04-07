FROM 3.11.3-alpine3.16 

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m", "flask", "--app", "./main", "run", "--host=0.0.0.0" ]