FROM httpd:2.4 
COPY ./dump/ /usr/local/apache2/htdocs/

FROM python:3.11

ADD scripts ./

RUN pip install -r requirements.txt

RUN playwright install

ENV PYTHONPATH ./scripts
ENV PYTHONUNBUFFERED 1

RUN bash

#CMD ["gunicorn", "-b", ":5000", "-t", "60", "-w", "1", "server:app"]

#EXPOSE 5000
