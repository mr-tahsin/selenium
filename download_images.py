import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set the path to chromedriver
chromedriver_path = r"G:\Tahsin\Automation_Selenium\chromedriver\chromedriver.exe"

# Set up Chrome options (Optional: Disable extensions, run in headless mode, etc.)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no UI)

# Initialize the Service object
service = Service(executable_path=chromedriver_path)

# Initialize the Chrome driver with the Service object and options
driver = webdriver.Chrome(service=service, options=options)

# URL of the image
image_url = "https://plus.unsplash.com/premium_photo-1664474619075-644dd191935f?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aW1hZ2V8ZW58MHx8MHx8fDA%3D"

# Folder to save the image
save_folder = r"G:\Tahsin\Automation_Selenium\tahsin\images"

# Ensure the folder exists
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Define the image filename
image_name = "downloaded_image_7.jpg"
image_path = os.path.join(save_folder, image_name)

# Download the image with SSL verification disabled
response = requests.get(image_url, verify=False)
if response.status_code == 200:
    with open(image_path, 'wb') as f:
        f.write(response.content)
    print(f"Image successfully downloaded to {image_path}")
else:
    print("Failed to download the image.")

# Close the browser (optional)
driver.quit()
