import os
import time
import requests
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# === CONFIG ===
STUDENT_NAME = 'ATHARVA GADKARI'
SEAT_NO = 'S400780203'
MOTHER_NAME = 'NIKITA'
TARGET_COURSE = "S.E.(2019 CREDIT PAT.) APR 2025"
CHROMEDRIVER_PATH = r"C:\webdrivers\chromedriver-win64\chromedriver.exe"
SAVE_DIR = os.path.join(os.getcwd(), "results")

# === SETUP CHROME ===
options = Options()
# options.add_argument("--headless")  # Disable headless for manual steps
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)

# === Step 1: Load Result Page ===
print("[INFO] Opening SPPU result portal...")
driver.get("https://onlineresults.unipune.ac.in/Result/Dashboard/Default")
time.sleep(3)

# === Step 2: Click 'Go for Result' for your target course ===
rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
for row in rows:
    if TARGET_COURSE in row.text:
        row.find_element(By.XPATH, ".//input[@value='Go for Result']").click()
        print("[INFO] Clicked 'Go for Result'")
        break

# === Step 3: Switch to Popup ===
time.sleep(2)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "Examination" in driver.title or "Result" in driver.title:
        print("[INFO] Switched to popup window")
        break

time.sleep(2)

# === Step 4: Auto click & fill fields ===
print("[INFO] Position mouse over Seat No input box in 5 seconds...")
time.sleep(5)

pyautogui.click()  # Clicks where your mouse is
time.sleep(1)

pyperclip.copy(SEAT_NO)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

print("[INFO] Now position mouse over Mother Name input in 5 seconds...")
time.sleep(5)

pyautogui.click()
time.sleep(1)

pyperclip.copy(MOTHER_NAME)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

print("[INFO] Please fill CAPTCHA and click 'Submit' manually.")

time.sleep(10)
# === Step 6: Type student name as filename ===
filename = STUDENT_NAME.replace(" ", "_") + "_Result.pdf"
pyperclip.copy(filename)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# === Step 7: Press Enter to save ===
pyautogui.press("enter")
print(f"✅ PDF should now be saving as: {filename}")
time.sleep(2)

# === Step 8: Close Browser ===
driver.quit()
