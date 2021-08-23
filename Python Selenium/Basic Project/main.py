from selenium import webdriver

DRIVER_PATH = r"C:\Users\Nikita\Documents\dev\msedgedriver.exe"
TEST_URL = r"https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html"

driver = webdriver.Edge(DRIVER_PATH)
driver.get(TEST_URL)
