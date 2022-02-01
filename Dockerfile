FROM python
RUN apt-get -qy update && apt-get -qy install \
        openssl \
        curl \
        build-essential \
        libc6-dev \

WORKDIR ./app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8777
