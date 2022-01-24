from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


#driver = webdriver.Chrome(executable_path="test/chromedriver")
driver = webdriver.Chrome(ChromeDriverManager().install())


def main_function():
    if test_score_service():
        print("Server is up")
        return 0
    else:
        print("Server is not responding")
        return -1
    

def test_score_service():
    app_url = open_driver("http://172.17.0.2:8777")
    between_range = check_score()
    driver.quit()
    return between_range

def open_driver(url):  
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-dev-shm-using")
    chromeOptions.add_argument("--disable-extensions")
    driver.get(url)
    app_url = driver.current_url
    chromeOptions.headless = True
    return app_url


def check_score():
    element1 = driver.find_element_by_id("score")
    return 1000 >= int(element1.text) >= 1


print(main_function())
