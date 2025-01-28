from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

    # Step 3: Wait for the welcome page to load
    WebDriverWait(driver, 15).until(
        EC.url_contains('Welcome.aspx')
    )
    print(f"Logged in successfully, current URL: {driver.current_url}")

    # Step 4: Navigate to the Salary Report subsection
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="nav"]/li[11]/a'))  # Main "Report" menu
    )
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[11]/a').click()  # Click the main menu

    # Click the "Salary Report" subsection
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="nav"]/li[11]/ul/li[5]/a'))  # Subsection XPath
    )
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[11]/ul/li[5]/a').click()

    # Step 5: Verify the final URL
    WebDriverWait(driver, 15).until(
        EC.url_contains('pageSalaryReport.aspx')  # Adjust if necessary
    )
    print(f"Final URL: {driver.current_url}")

    # Step 6: Select "Emp Pay slip" from the Report Type dropdown
    report_type_dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlReportType-container"]'))
    )
    report_type_dropdown.click()
    report_type_option = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//li[text()="Emp Pay slip"]'))
    )
    report_type_option.click()
    print("Emp Pay slip selected successfully.")

    # Step 7: Wait for 5 seconds to allow other dropdowns to load
    time.sleep(5)

    # Step 8: Select the radio button
    radio_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ContentPlaceHolder1_radUnit"]'))
    )
    radio_button.click()
    print("Radio button selected successfully.")

    # Step 9: Select "MPL Wear" from the "Unit" dropdown
    try:
        # Click on the dropdown to make options visible
        unit_dropdown = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlUnit-container"]'))
        )
        unit_dropdown.click()

        # Wait for the dropdown options to load and select "MPL Wear"
        unit_option = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//li[contains(text(), "MPL Wear")]'))
        )
        unit_option.click()
        print("MPL Wear selected successfully.")
    except Exception as e:
        print(f"Error during unit dropdown selection: {e}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Optional: Keep the browser open or close it
    # driver.quit()
    pass
