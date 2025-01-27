import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Path to your ChromeDriver executable
chromedriver_path = "G:/Tahsin/Automation_Selenium/chromedriver/chromedriver.exe"

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Use the specified ChromeDriver path
service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Open the login page
    driver.get('https://mis-hris.mascoknit.com/logIn.aspx')

    # Step 2: Wait for the username field and input credentials
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_txtUserId"]'))
    )
    username = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtUserId"]')
    username.send_keys('184288')

    password = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPassword"]')
    password.send_keys('t@hs1n')

    # Step 3: Click the login button
    btn = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_btnLogin"]')
    btn.click()

    # Step 4: Navigate to the salary report page
    WebDriverWait(driver, 15).until(
        EC.url_contains("https://mis-hris.mascoknit.com/")
    )
    driver.get('https://mis-hris.mascoknit.com/pageSalaryReport.aspx')

    print("Navigation successful!")

except Exception as e:
    print(f"Error during navigation: {e}")

finally:
    # Optional: Close the driver after testing
    pass
