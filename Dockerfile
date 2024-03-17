FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENV PORT 80
EXPOSE 80

CMD ["python", "main.py"]