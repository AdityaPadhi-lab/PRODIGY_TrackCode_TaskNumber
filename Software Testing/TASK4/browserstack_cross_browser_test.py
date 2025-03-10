from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# BrowserStack capabilities (Replace with your credentials)
browserstack_options = {
    "os": "Windows",
    "os_version": "10",
    "browser": "Chrome",
    "browser_version": "latest",
    "name": "Cross-Browser Login Test"
}

# Initialize WebDriver with BrowserStack
driver = webdriver.Remote(
    command_executor="https://USERNAME:ACCESS_KEY@hub-cloud.browserstack.com/wd/hub",
    options=webdriver.ChromeOptions()
)

# Open test website
driver.get("https://example.com/login")

# Perform login test
driver.find_element(By.ID, "username").send_keys("test_user")
driver.find_element(By.ID, "password").send_keys("test_password")
driver.find_element(By.ID, "login_button").click()
time.sleep(2)

# Verify login success
if "dashboard" in driver.current_url:
    print("Test Passed: Login works on BrowserStack")
else:
    print("Test Failed: Login did not work on BrowserStack")

driver.quit()
