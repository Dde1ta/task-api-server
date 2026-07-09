FROM python:3.14-alpine

RUN mkdir "app"

WORKDIR "/app"

COPY . "/app"

RUN pip install -r requirments.txt

CMD ["uvicorn", "main:app"]