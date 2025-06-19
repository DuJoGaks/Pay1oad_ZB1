FROM python:3.8.13-slim

WORKDIR /App

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","manage.py","runserver","0.0.0.0:8000"]