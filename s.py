# download hourly leave Form from the Masco search engine

import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Reusable function for waiting for elements to be clickable
def wait_for_element(driver, by, value, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    except Exception as e:
        print(f"Error waiting for element ({by}, {value}): {e}")
        return None

# Setup WebDriver with specific chromedriver location
chromedriver_path = 'G:/Tahsin/Automation_Selenium/chromedriver/chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)

# Use the specified chromedriver location
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open login page
driver.get('https://mis-search.mascoknit.com/LogIn/LogIn')

# Step 2: Input username and password
username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
username.send_keys('184288')

password = driver.find_element(By.XPATH, '//*[@id="txtPass"]')
password.send_keys('t@hs1n')

# Step 3: Click login button
btn = driver.find_element(By.XPATH, '//*[@id="btnLogin"]')
btn.click()

# Step 4: Wait for the dropdown options to load and select
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ddlMascoSrcDrop"]/option'))
    )
    print("Dropdown options loaded.")

    # Interact with the dropdown
    dropdown = driver.find_element(By.XPATH, '//*[@id="ddlMascoSrcDrop"]')
    select = Select(dropdown)
    select.select_by_visible_text('Personal Documents Download Section')
    print("Option selected successfully.")

except Exception as e:
    print(f"Dropdown selection error: {e}")

# Step 5: Wait for and click the search button
selbtn = wait_for_element(driver, By.XPATH, '//*[@id="btnSearch"]')
if selbtn:
    selbtn.click()
    print("Search button clicked successfully.")

    # Step 6: Wait for the next page to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="btnHourlyLeave"]'))
        )
        print("Next page loaded after search.")
    except Exception as e:
        print(f"Error while waiting for next page: {e}")

# Step 7: Click the "Short Leave" button (on the new page)
selbtn1 = wait_for_element(driver, By.XPATH, '//*[@id="btnHourlyLeave"]')
if selbtn1:
    selbtn1.click()
    print("Short leave button clicked successfully.")

# Step 8: Handle the new tab
try:
    # Save the current window handle
    original_window = driver.current_window_handle
    print(f"Original window handle: {original_window}")

    # Wait for the new tab to open
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Log available window handles
    print(f"Available window handles before switching: {driver.window_handles}")

    # Switch to the new tab
    new_tab = [window for window in driver.window_handles if window != original_window][0]
    driver.switch_to.window(new_tab)
    print(f"Switched to new tab with handle: {new_tab}")

    # Wait for the page to fully load in the new tab before looking for the button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnDownload"]')))
    print("Page fully loaded in new tab.")

    # Wait for the "Download" button to be clickable in the new tab
    download_btn = wait_for_element(driver, By.XPATH, '//*[@id="btnDownload"]')
    if download_btn:
        download_btn.click()
        print("Download button clicked successfully.")
    else:
        print("Download button not found or not clickable in the new tab.")

    # Optionally, close the new tab and switch back to the original tab
    driver.close()
    driver.switch_to.window(original_window)
    print("Switched back to the original window.")

except Exception as e:
    print(f"Error while handling new tab: {e}")
    print(f"Current window handles: {driver.window_handles}")
