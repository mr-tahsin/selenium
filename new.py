from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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

    # Step 6: Select the "Unit" dropdown and choose "MPL Wear"
    unit_dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlUnit-container"]'))
    )
    unit_dropdown.click()
    unit_option = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlUnit-results"]/li[text()="MPL Wear"]'))
    )
    unit_option.click()
    print("MPL Wear selected successfully.")

    # Step 7: Select "Emp Pay slip" from the Report Type dropdown
    report_type_dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlReportType-container"]'))
    )
    report_type_dropdown.click()
    report_type_option = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlReportType-results"]/li[text()="Emp Pay slip"]'))
    )
    report_type_option.click()
    print("Emp Pay slip selected successfully.")

    # Step 8: Select "2025-2025" from the Financial Year dropdown
    fin_year_dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlFinYear-container"]'))
    )
    fin_year_dropdown.click()
    fin_year_option = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlFinYear-results"]/li[text()="2025-2025"]'))
    )
    fin_year_option.click()
    print("2025-2025 Financial Year selected successfully.")

    # Step 9: Select "December" from the Month dropdown
    month_dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlMonth-container"]'))
    )
    month_dropdown.click()
    month_option = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlMonth-results"]/li[text()="December"]'))
    )
    month_option.click()
    print("December month selected successfully.")

    # Step 10: Click the first radio button
    radio_button_1 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ContentPlaceHolder1_iddivCop"]/div[2]/label[2]'))
    )
    radio_button_1.click()
    print("First radio button selected successfully.")

    # Step 11: Click the second radio button
    radio_button_2 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="UpdatePanel1"]/div/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/div[6]/label[2]'))
    )
    radio_button_2.click()
    print("Second radio button selected successfully.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Optional: Keep the browser open or close it
    # driver.quit()
    pass
