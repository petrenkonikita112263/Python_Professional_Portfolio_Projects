from selenium import webdriver

DRIVER_PATH = r"C:\Users\Nikita\Documents\dev\msedgedriver.exe"
URL_LINK = r"https://www.seleniumeasy.com/test/basic-first-form-demo.html"

driver = webdriver.Edge(DRIVER_PATH)
driver.get(URL_LINK)
driver.implicitly_wait(20)
close_button = driver.find_element_by_id("at-cv-lightbox-close")
close_button.click()
