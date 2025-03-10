from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed

# Open e-commerce website
driver.get("https://example.com")  # Replace with actual URL

# Test: Add Item to Cart
driver.find_element(By.ID, "add_to_cart_button").click()
time.sleep(1)

# Test: Proceed to Checkout
driver.find_element(By.ID, "checkout_button").click()
time.sleep(1)

# Test: Fill out checkout form
driver.find_element(By.ID, "name").send_keys("John Doe")
driver.find_element(By.ID, "email").send_keys("john@example.com")
driver.find_element(By.ID, "address").send_keys("123 Main St")
driver.find_element(By.ID, "credit_card").send_keys("4111111111111111")
driver.find_element(By.ID, "submit_order").click()
time.sleep(3)

# Verify Success Message
if "Order placed successfully" in driver.page_source:
    print("Test Passed: Checkout process completed")
else:
    print("Test Failed: Checkout process failed")

# Close browser
driver.quit()
