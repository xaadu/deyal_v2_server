FROM python:3.10.12-alpine
ENV PYTHONUNBUFFERED 1

RUN apk --update add bash && apk --no-cache add dos2unix

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN dos2unix ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

CMD [ "sh", "./entrypoint.sh" ]
