from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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
        EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtUserId"))
    ).send_keys('184288')

    driver.find_element(By.ID, "ContentPlaceHolder1_txtPassword").send_keys('t@hs1n')
    driver.find_element(By.ID, "ContentPlaceHolder1_btnLogin").click()

    # Step 3: Wait for login success
    WebDriverWait(driver, 15).until(
        EC.url_contains('Welcome.aspx')  # Ensure login was successful
    )
    print(f"Login successful, current URL: {driver.current_url}")

    # Step 4: Capture cookies after login
    cookies = driver.get_cookies()

    # Step 5: Navigate to Corporate Information Mailing page
    driver.get('https://mis-hris.mascoknit.com/pageMailSendPanel.aspx')

    # Step 6: Add cookies to maintain session
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Step 7: Refresh the page
    driver.refresh()

    # Step 8: Ensure correct page loads
    WebDriverWait(driver, 15).until(
        EC.url_to_be('https://mis-hris.mascoknit.com/pageMailSendPanel.aspx')
    )
    print(f"Navigated to Corporate Information Mailing page: {driver.current_url}")

    # Step 9: Select "Monthly Pay Slip" from dropdown
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlSelectOption-container"]'))
    ).click()

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "Monthly Pay Slip")]'))
    ).click()
    print("Selected 'Monthly Pay Slip' from the dropdown.")

    # Step 10: Select "2025-2025" from financial year dropdown
    try:
        # Wait for dropdown to be present
        fin_year_dropdown = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddlFinYear"))
        )

        # Use Select class to choose option by value
        select = Select(fin_year_dropdown)
        select.select_by_value("13")  # Corrected value for "2025-2025"

        print("Successfully selected '2025-2025' from the Fin Year dropdown.")

    except Exception as e:
        print(f"Error while selecting financial year: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    pass  # You can use driver.quit() if needed
