FROM python:3.12.9

WORKDIR /v1/src

ENV PYTHONPATH=/v1/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python v1/src/main.py"]

