from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time 

def find_element_with_retry(driver, locator, retries=3):
    for _ in range(retries):
        try:
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except StaleElementReferenceException:
            continue
    raise Exception("Element not found after retries")

options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://60.174.0.143:8089")
driver = webdriver.Chrome(options=options)
# driver.get("http://www.python.org")
driver.get("https://www.zhipin.com/shanghai/?ka=city-sites-101020100")
# print driver title
print(driver.title)
elems = driver.find_elements(By.CLASS_NAME,"ipt-search")

elems[0].send_keys("devops")
elems[0].send_keys(Keys.ENTER)




# wait 
# wait = WebDriverWait(driver=driver,timeout=10)

# element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[ka='switch_city_dialog_open']")))

# element.click()

# new_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='上海']"))

# new_option.click()

# search_input_box_locator = (By.CLASS_NAME,"search-input-box input")

# search_input_box = find_element_with_retry(driver,search_input_box_locator)

# print(search_input_box)





# cities = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"city-list-hot")))

# print(cities)


# for city in cities:
#     print(city)
# time.sleep(5)

# input_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME("search-input-box"))))


# input_element.send_keys("golang运维工程师")




time.sleep(100)



# elements = driver.find_elements(by=By.CLASS_NAME,value="city-label")
# print(elements[0].text)


# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
