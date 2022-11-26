FROM python:3.10

WORKDIR /coursedwork_5
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD gunicorn --bind 0.0.0.0:80 --access-logfile='-' --capture-output app:app

# docker build -t my_custom .
# docker run my_custom