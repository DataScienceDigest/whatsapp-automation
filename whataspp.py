

from selenium import webdriver
import pyautogui
from selenium.webdriver.chrome.options import Options
import random
import pyperclip
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get("https://web.whatsapp.com/")

sleep(10)  # Time to scan the QR code

contacts = [
    "9888786469", "9464043343", "7837236418", ]

image_path = r"C:\Users\Acer\Desktop\SEND IMAGE.jpeg"  # Path to your image

failed_contacts = []

for i in contacts:
    try:
        # Locate the input element for searching contacts
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @role='textbox']"))
        )
        
        # Clear any previous text and enter new contact
        input_element.click()
        input_element.clear()
        sleep(1)
        input_element.send_keys(i)
        sleep(2)
        input_element.send_keys(Keys.ENTER)
        print(f"Opened chat with {i}")
        sleep(3)

        # Proceed to send the image and caption
        plus_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.x11xpdln.x1d8287x.x1h4ghdb span[data-icon='plus']"))
        )
        plus_button.click()
        sleep(2)

        # Select "Photos & videos" and upload the image
        photos_videos_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Photos & videos']"))
        )
        photos_videos_option.click()
        sleep(2)
        pyautogui.write(image_path, interval=0.1)
        pyautogui.press('enter')

        # Enter caption
        caption_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-placeholder='Add a caption']"))
        )
        caption_box.click()
        caption_text = ("🚀 Join Our Best Industrial Training Program! 🌟  "
                        "! 🌟 📍 Locations: Jalandhar | Hoshiarpur | Phagwara "
                        "📚 Courses: AI, Cyber Security, Data Science, MERN, Digital Marketing & more!  "
                        "💼 100% Placement Support ✅"
                        "📞 Contact: 9888122255 📱 "
                        "🔗 Start your journey to success today! ✨")
        pyperclip.copy(caption_text)
        sleep(1)
        caption_box.send_keys(Keys.CONTROL, 'v')
        sleep(1)
        caption_box.send_keys(Keys.ENTER)
        print(f"Message sent to {i}")

    except Exception as e:
        print(f"Error with contact {i}: {e}")
        failed_contacts.append(i)
        
    finally:
        # Clear the input element after each attempt to avoid leftover text
        try:
            # Re-locate the input element to make sure it's accessible
            input_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @role='textbox']"))
            )
            input_element.click()  # Click to make sure it's focused
            sleep(1)  # Brief delay to ensure the click registers

            # Use Ctrl + A (Select All) and then Delete to clear any leftover text
            input_element.send_keys(Keys.CONTROL, 'a')  # Select all text
            input_element.send_keys(Keys.DELETE)         # Delete the selected text
            print("Input fully cleared for the next contact")
        except Exception as clear_error:
            print(f"Failed to clear input for next contact: {clear_error}")

# Report contacts with errors
if failed_contacts:
    print("\nContacts with failed attempts:")
    for contact in failed_contacts:
        print(contact)
else:
    print("\nAll contacts processed successfully!")
