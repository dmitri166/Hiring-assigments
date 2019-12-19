FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

EXPOSE 9405
COPY stats.py ./
CMD ["gunicorn", "-b", "0.0.0.0:9405", "-t", "180", "--access-logfile", "-", "stats:app"]
