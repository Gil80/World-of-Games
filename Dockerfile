FROM python
WORKDIR ./app
RUN CHROMEDRIVER_VERSION=curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/bin && \ 
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip  RUN apt install libgbm1 -y && \
    CHROME_SETUP=google-chrome.deb && \
    wget -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    dpkg -i $CHROME_SETUP && \
    apt-get install -y -f && \
    rm $CHROME_SETUP
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8777
