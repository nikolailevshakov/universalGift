FROM python:3.7-alpine

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 80

CMD ["python", "main.py"]