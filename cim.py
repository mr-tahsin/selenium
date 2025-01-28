from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver
chromedriver_path = "G:/Tahsin/Automation_Selenium/chromedriver/chromedriver.exe"

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keeps browser open after script ends

service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Open login page
    driver.get('https://mis-hris.mascoknit.com/logIn.aspx')

    # Step 2: Input credentials and log in
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_txtUserId"]'))
    )
    driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtUserId"]').send_keys('184288')
    driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPassword"]').send_keys('t@hs1n')
    driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_btnLogin"]').click()

    # Step 3: Wait for login success
    WebDriverWait(driver, 15).until(
        EC.url_contains('Welcome.aspx')  # Ensure the login was successful and the page redirected
    )
    print(f"Login successful, current URL: {driver.current_url}")

    # Step 4: Capture cookies after login
    cookies = driver.get_cookies()

    # Step 5: Directly navigate to Corporate Information Mailing page
    driver.get('https://mis-hris.mascoknit.com/pageMailSendPanel.aspx')

    # Step 6: Add the captured cookies to maintain the session
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Step 7: Refresh the page to maintain the session after setting the cookies
    driver.refresh()

    # Step 8: Wait for the page to load
    WebDriverWait(driver, 15).until(
        EC.url_to_be('https://mis-hris.mascoknit.com/pageMailSendPanel.aspx')
    )
    print(f"Navigated directly to Corporate Information Mailing page: {driver.current_url}")

    # Step 9: Select the dropdown and choose an option
    # Wait for the dropdown to be clickable
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlSelectOption-container"]'))
    )
    
    # Click the dropdown
    dropdown = driver.find_element(By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlSelectOption-container"]')
    dropdown.click()

    # Select Monthly Pay Slip from the dropdown
    option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "Monthly Pay Slip")]'))
    )
    option.click()

    print("Dropdown option selected successfully.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Comment the quit line for debugging purposes
    # driver.quit()
    pass

