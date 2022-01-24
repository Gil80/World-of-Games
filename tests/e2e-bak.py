from selenium import webdriver
import sys

from selenium.webdriver.chrome.service import Service


url = 'http://172.17.0.2:8777'


def test_score_service():
    try:
        s = Service(executable_path="/tmp/tests/chromedriver")
        my_driver = webdriver.Chrome(service=s)
        my_driver.get(url)
        score = int(my_driver.find_element_by_id("score").text)
        return 0 <= score <= 1000
    except BaseException:
        print("cannot open the server")


def main_function():
    if test_score_service():
        print(0)
        return sys.exit(0)
    else:
        print(-1)
        return sys.exit(-1)



if __name__ == '__main__':
    main_function()