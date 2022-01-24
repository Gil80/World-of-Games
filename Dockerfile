FROM python:3.8-slim-buster

#RUN pip install selenium
## install google chrome
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
#RUN apt-get -y update
#RUN apt-get install -y google-chrome-stable
#
# install chromedriver
#UN apt-get install -yqq unzip
#UN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
#UN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
#
# install requirements
RUN python -m pip install --upgrade pip
#RUN pip install --no-cache-dir getpass3
#RUN pip install --no-cache-dir requests
#RUN pip install --no-cache-dir flask
#RUN pip install --no-cache-dir utils


#RUN useradd --create-home wog

#USER wog

## activate virtual environment
#ENV VIRTUAL_ENV=/home/wog/env
#ENV PATH="/home/wog/venv/bin:$PATH"
EXPOSE 8777

# Set the working directory to /app
WORKDIR /app
COPY ["MainScores.py", "Scores.py", "Scores.txt", "Utils.py", "requirements.txt", "/app/"]
COPY "tests/e2e.py" "/app/tests/"
COPY "tests/chromedriver" "tests/chromedriver"
COPY templates/ /app/templates
RUN pip3 install -r requirements.txt


CMD ["python3", "MainScores.py"]
CMD ["python3", "tests/e2e.py"]

