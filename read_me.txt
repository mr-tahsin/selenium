masco.py old script...
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options with headless mode
download_path = r"G:\Tahsin\Automation_Selenium\tahsin\images"
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})
# chrome_options.add_argument("--headless")  # Headless mode

# Provide the path to ChromeDriver
service = Service(r"G:\Tahsin\Automation_Selenium\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    print("Navigating to login page...")
    driver.get("https://mis-hris.mascoknit.com/")

    # Wait for the login elements to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtUserId")))
    print("Login elements found")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtPassword")))
    print("Password field found")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_btnLogin")))
    print("Login button clickable")

    # Step 2: Log in
    driver.find_element(By.ID, "ContentPlaceHolder1_txtUserId").send_keys("184288")
    driver.find_element(By.ID, "ContentPlaceHolder1_txtPassword").send_keys("t@hs1n")
    driver.find_element(By.ID, "ContentPlaceHolder1_btnLogin").click()

    # Step 3: Wait for successful login or page redirection
    WebDriverWait(driver, 20).until(EC.url_contains("pageSalaryReport.aspx"))
    print("Navigated to salary report page")

except Exception as e:
    print(f"An error occurred: {e}")

# Keep the browser open after the script finishes execution
input("Press Enter to close the browser...")
