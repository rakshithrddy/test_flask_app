FROM python:3.9-alpine
RUN apk update
RUN apk add --no-cache \
    gcc \
    musl-dev \  
    python3 \        
    py3-pip

WORKDIR /flask_app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]

