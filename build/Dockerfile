FROM python:3.8

ENV PYTHONUNBUFFERED=1
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin python3-gdal
ADD ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -U pip && pip install --cache-dir /root/.cache/pip -r ./requirements.txt
CMD ["python", "manage.py", "runserver", "--insecure"]