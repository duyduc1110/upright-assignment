FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
EXPOSE 18000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "18000"]