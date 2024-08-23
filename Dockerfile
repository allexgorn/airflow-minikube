FROM tensorflow/tensorflow:latest

WORKDIR /app

COPY modelFashion.py /app/modelFashion.py

CMD ["python", "/app/modelFashion.py"]

