from selenium import webdriver

DRIVER_PATH = r"C:\Users\Nikita\Documents\dev\msedgedriver.exe"
URL_LINK = r"https://www.seleniumeasy.com/test/basic-first-form-demo.html"

driver = webdriver.Edge(DRIVER_PATH)
driver.get(URL_LINK)
driver.implicitly_wait(20)
try:
    close_button = driver.find_element_by_id("at-cv-lightbox-close")
    close_button.click()
except:
    print("No element was found with the provided id")

sum_1 = driver.find_element_by_id("sum1")
sum_2 = driver.find_element_by_id("sum2")

sum_1.send_keys(15)
sum_2.send_keys(15)
