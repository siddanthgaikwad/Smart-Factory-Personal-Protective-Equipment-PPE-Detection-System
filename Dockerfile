FROM python:3.10

WORKDIR /app

# 🔥 install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
EXPOSE 8000

CMD ["streamlit", "run", "app/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]