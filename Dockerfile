CMD ["python", "app.py"]
>>>>>>> da5eafd21d1c940d075d2bb51d327324903b97e9
=======
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
=======
CMD ["python", "app.py"]
>>>>>>> da5eafd21d1c940d075d2bb51d327324903b97e9
