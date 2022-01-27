from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager  # Use this for local run only.
import sys

#chrome_driver = webdriver.Chrome(ChromeDriverManager().install())  # Use this for local run only.

#chrome_driver = webdriver.Chrome('/home/gil/projects/WorldOfGames/chromedriver')

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
#chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
chromeOptions.headless = True
chrome_driver = webdriver.Chrome(options=chromeOptions)  # comment this line when running locally.

url = 'http://172.17.0.2:8777'


def test_score_service():
    try:
        chrome_driver.get(url)
        score = int(chrome_driver.find_element(By.ID, "score").text)
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