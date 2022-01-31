FROM moditamam/selenium:python3

RUN apt-get update && apt-get install -y procps less wget

RUN apt-get install -y python3 python3-pip

WORKDIR /app

COPY . /app

EXPOSE 8777

RUN pip3 install -r requirements.txt

CMD python3 MainScores.py
