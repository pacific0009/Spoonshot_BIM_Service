FROM python:3.6-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


# Installing requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Adding remaining files
ADD . .

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

# ENTRYPOINT ["bash", "/usr/src/app/docker-entrypoint.sh"]

