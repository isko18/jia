FROM python:3.10
LABEL authors="Isko"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /BIF

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y supervisor && \
    rm -rf /var/lib/apt/lists/*

COPY . /BIF
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY create_superuser.py /usr/local/bin/create_superuser.py

CMD ["bash", "-c", "python manage.py migrate && python /usr/local/bin/create_superuser.py && /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf"]
