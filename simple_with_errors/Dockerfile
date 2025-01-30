FROM python:slim-bullseye

WORKDIR /script

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY script.py genomeC.fna .

CMD ["python", "script.py"]