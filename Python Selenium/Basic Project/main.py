from selenium import webdriver

DRIVER_PATH = r"C:\Users\Nikita\Documents\dev\msedgedriver.exe"
TEST_URL = r"https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html"

driver = webdriver.Edge(DRIVER_PATH)
driver.get(TEST_URL)
driver.implicitly_wait(15)
button = driver.find_element_by_id("downloadButton")
button.click()

progress_msg = driver.find_element_by_class_name("progress-label")
print(f"{progress_msg.text}")
