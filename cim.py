import threading
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

def login():
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
    except Exception as e:
        print(f"Error during login: {e}")

def select_financial_year():
    try:
        # Step 4: Select Financial Year
        fin_year_dropdown = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddlFinYear"))
        )
        Select(fin_year_dropdown).select_by_visible_text("2025-2025")
        print("Successfully selected '2025-2025' from the Fin Year dropdown.")
    except Exception as e:
        print(f"Error while selecting financial year: {e}")

def select_monthly_pay_slip():
    try:
        # Step 5: Select Monthly Pay Slip
        dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-ContentPlaceHolder1_ddlSelectOption-container"]'))
        )
        dropdown.click()

        # Wait for the dropdown options to be visible and select the first option ("Monthly Pay Slip")
        first_option = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//ul[@id="select2-ContentPlaceHolder1_ddlSelectOption-results"]/li[1]'))
        )
        first_option.click()

        print("Successfully selected 'Monthly Pay Slip' from the dropdown.")
    except Exception as e:
        print(f"Error while selecting Monthly Pay Slip: {e}")

def main():
    try:
        # Step 6: Login and navigate
        login()

        # Step 7: Capture cookies after login
        cookies = driver.get_cookies()

        # Step 8: Navigate to Corporate Information Mailing page
        driver.get('https://mis-hris.mascoknit.com/pageMailSendPanel.aspx')

        # Step 9: Add cookies to maintain session
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Step 10: Refresh the page
        driver.refresh()

        # Step 11: Wait for the page to load
        WebDriverWait(driver, 15).until(
            EC.url_to_be('https://mis-hris.mascoknit.com/pageMailSendPanel.aspx')
        )
        print(f"Navigated to Corporate Information Mailing page: {driver.current_url}")

        # Step 12: Execute functions concurrently using threading
        thread1 = threading.Thread(target=select_financial_year)
        thread2 = threading.Thread(target=select_monthly_pay_slip)

        thread1.start()
        thread2.start()

        # Wait for both threads to finish
        thread1.join()
        thread2.join()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pass  # Optionally, you can close the driver with driver.quit()

if __name__ == "__main__":
    main()
