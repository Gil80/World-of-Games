
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def main_function():
    if test_score_service():
        return 0
    else:
        return -1
    

def test_score_service():
    app_url = open_driver("http://127.0.0.1:5000")
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
