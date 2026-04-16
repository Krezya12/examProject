FROM python:3.13-alpine
WORKDIR /app
COPY . .
RUN pip install -r req.txt
CMD ["python3", "main.py"]