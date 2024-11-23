

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
    "9888786469", "9464043343", "7837236418", "8194903224", "8795738026", "6239737732", "9872480141", "9041136631", "8360238648", "6239215235", "9417090687", "7404726384", "9915443265", "9872994864", "9870706511", "7006074105", "8968780761", "9915765411", "8528255372", "9415435889", "8360959715", "9464923494", "7087131307", "9779077697", "7710533894", "8968182976", "6283339609", "9877835546", "8284889718", "9815177952", "9988963352", "8284914650", "8699375819", "9815177952", "7717240607", "7085773501", "7837991079", "9888621740", "7876074273", "8699191466", "9872921775", "9041514679", "8556879970", "6289212843", "8725955019", "9700099306", "8699965240", "9478004558", "8360086469", "8360086469", "9781461821", "8699965240", "9041566203", "9888759498", "6202187680", "9609193493", "7347429327", "7814523914", "8437358297", "6203544344", "6284555749", "8292001980", "9814447072", "9888774544", "9530575966", "7814790268", "8427562402", "8264168720", "7986473124", "8195953671", "7696266229", "919502000000", "9115536202", "918427000000", "917301000000", "919646000000", "919806000000", "6207069865", "919988000000", "919877000000", "917711000000", "918838000000", "919973000000", "917815000000", "919816000000", "919199000000", "919779000000", "917889000000", "919873000000", "917720000000", "919417000000", "917405000000", "919915000000", "919873000000", "7696691499", "9817124897", "7707866136", "7706850054", "6283919045", "9780555969", "6290658874", "6006152557", "9501349228", "7888956935", "6206267902", "7015677474", "6283517532", "9464426607", "6283924176", "7696718220", "6284849925", "917743000000", "919418000000", "917308000000", "919418000000", "919889000000", "9592954831", "9041218147", "8864070891", "9915319573", "8146361413", "8968944525", "8872555111", "9357414343", "9091256884", "7743033477", "8360042884", "8872555111", "7404792657", "919041000000", "919347000000", "918968000000", "7888976229", "9814350302", "7814750631", "6283914876", "9334921027", "7009062995", "8264964054", "8847214960", "9814327361", "8872964729", "7696582931", "9878771692", "8847069925", "8699213368", "9877057919", "9041677738", "9888396763", "9876375342", "6239337901", "9041272382", "7529892505", "9988200658", "8360433665", "7501510386", "9501481894", "9814326106", "9417381993", "7901823271", "7254994947", "8228084217", "6280624226", "766870196", "9878768156", "7088542996", "9803905695", "9814525888", "8102860972", "9877329182", "6284809715", "9814387131", "9463539868", "6283584465", "8968106794", "8839771611", "7087383471", "6284961462", "9914075181", "8427502575", "8294277757", "7658825233", "9872010231", "7837989830", "9417183775", "8699919406", "9876705070", "9463031880", "7657942817", "9779519407", "6239051963", "7814064869", "9878960748", "8427903724", "7347339435", "8146557593", "6200108773", "7340920749", "9915462602", "8847573762", "6239637001", "7759076568", "9877936239", "9056208385", "8558047940", "9592348649", "9876485699", "9779437497", "9464482479", "8872613901", "8102446878", "7651973679", "9878282582", "9814193924", "8146595115", "9872180373", "9915444754", "6284839830", "9115885360", "8968543454", "7508558294", "9872097927", "9966457739", "7009940533", "9592914280", "7668115956", "8198035753", "9478753092", "9501462441", "9601683813", "9815678347", "9417234499", "9915827588", "6239394396", "9988569409", "9501656266", "9827868134", "9478262232", "8699156569", "9056346866", "6283760755", "7719416729", "6283021210", "8968096065", "9815083978", "9876497321", "9229847230", "9815615916", "9888239530", "9056484093", "9781792108", "6239161540", "8708390264", "6280804933", "6280931221", "7818049409", "7087915196", "8194916150", "9115884742", "9041272382", "9878888076", "6280462576", "9888870120", "8679432425", "9155357141", "7545860400", "9463892980", "8054356823", "9815808466", "6296486395", "9797617681"
]

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
