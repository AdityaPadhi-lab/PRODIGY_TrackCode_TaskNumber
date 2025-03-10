from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed

# Open the login page
driver.get("https://example.com/login")  # Replace with actual login URL

# Test Case 1: Valid Login
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_password")
driver.find_element(By.ID, "login_button").click()
time.sleep(2)

# Check if login successful
if "dashboard" in driver.current_url:
    print("Test Passed: Valid login successful")
else:
    print("Test Failed: Valid login unsuccessful")

# Test Case 2: Invalid Login
driver.get("https://example.com/login")  # Reload page
driver.find_element(By.ID, "username").send_keys("invalid_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")
driver.find_element(By.ID, "login_button").click()
time.sleep(2)

if "Invalid credentials" in driver.page_source:
    print("Test Passed: Invalid login error message displayed")
else:
    print("Test Failed: Error message not shown")

# Close browser
driver.quit()
