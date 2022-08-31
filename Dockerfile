FROM python:3.10

WORKDIR /home/app

RUN apt update

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "src/main.py" ]

EXPOSE 3456
