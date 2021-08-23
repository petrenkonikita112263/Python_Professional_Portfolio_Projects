from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DRIVER_PATH = r"C:\Users\Nikita\Documents\dev\msedgedriver.exe"
TEST_URL = r"https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html"

driver = webdriver.Edge(DRIVER_PATH)
driver.get(TEST_URL)
driver.implicitly_wait(15)
button = driver.find_element_by_id("downloadButton")
button.click()

# explicit wait - 30 seconds until the condition (text in progress bar would be Complete) is archived
WebDriverWait(driver, 30).until(
    ec.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"),                  # element filtration
        "Complete!"                                         # expected text
    )
)
