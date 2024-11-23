# WhatsApp Automation Script

This Python project automates the process of sending images with captions to multiple WhatsApp contacts using Selenium and PyAutoGUI. It is designed to streamline repetitive tasks, such as sending promotional messages, alerts, or updates to a list of users.

---

## Features

- **Automated Messaging**: Sends a pre-written message and an image to multiple contacts via WhatsApp Web.
- **Error Handling**: Logs failed attempts to a list for review and retry.
- **Dynamic Captions**: Allows custom captions for the image.
- **Contact Search**: Automatically searches for contacts using their phone numbers.
- **Input Clearing**: Ensures the search input is cleared after each attempt.

---

## Prerequisites

### Software Requirements
- **Python 3.x**
- **Google Chrome Browser** (Ensure the version matches the ChromeDriver used)
- **ChromeDriver** (Download from [ChromeDriver](https://chromedriver.chromium.org/downloads))

### Python Libraries
- `selenium`
- `pyautogui`
- `pyperclip`

Install the required libraries using:
```bash
pip install selenium pyautogui pyperclip
git clone https://github.com/DataScienceDigest/whatsapp-automation.git
cd whatsapp-automation
python whatsapp_automation.py
