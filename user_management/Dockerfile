FROM python:3.10-slim

WORKDIR /app

# Copiar el archivo de dependencias desde el directorio raíz
COPY ../../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app

CMD ["python", "app.py"]
