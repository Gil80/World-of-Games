FROM gil80/py-flask:v4.5
WORKDIR ./app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8777
