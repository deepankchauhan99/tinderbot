import datetime
import subprocess
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Uncomment if you want to open browser and watch it happening
# command = [
#     '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
#     '--remote-debugging-port=9222',
#     '--user-data-dir=/Users/deepank/Documents/Python Projects/Tinderbot/.chrome-session'
# ]
# subprocess.Popen(command)

web = 'https://tinder.com/'

options = Options()
# Uncomment if you want to open browser and watch it happening
# options.add_experimental_option("debuggerAddress", "localhost:9222")

# Comment if want to open browser and watch it happening
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=/Users/deepank/Documents/Python Projects/Tinderbot/.chrome-session")


driver = webdriver.Chrome(options=options)


pickup_lines = [
    "I'm always up for a late-night drive with good company and ice cream. What's your idea of a perfect evening?",
    "If you enjoy late-night conversations and ice cream as much as I do, we might just be a great match.",
    "I'm a software engineer who loves a good ice cream run. If you're into spontaneous adventures, let's chat!",
    "Driving around town looking for the best ice cream spot sounds like a fun adventure. Care to join me?",
    "Late-night drives and ice cream are my kind of fun. How do you like to unwind after a long day?",
    "I'm always up for trying new ice cream flavors. Want to share your favorite one with me?",
    "If you love late-night drives and sweet treats as much as I do, we might have a lot in common.",
    "I believe every great conversation starts with good ice cream. What's your favorite flavor to enjoy on a chill night?",
    "As a software engineer, I appreciate good code and great company. Let's see if we click as well as my favorite ice cream flavors do!",
    "I'm a fan of spontaneous late-night adventures and ice cream. What's your idea of a fun night out?"
]
number_of_swipes = 25

time.sleep(2)

driver.get(web)
print(datetime.datetime.now())
print("Browser opened!")
print("Site opened!")
time.sleep(3)


for i in range(number_of_swipes):

    try:
        like_button = driver.find_element(by='xpath', value='//button//span[text()="Like"]')
        driver.execute_script("arguments[0]?.click();", like_button)
        time.sleep(3)
        print("Liked: " + str(i + 1))

        its_match_window = driver.find_element(by='xpath', value='//textarea[@placeholder="Say something nice!')
        message = random.choice(pickup_lines)
        its_match_window.send_keys(message)
        time.sleep(1)
        print("Matched: " + str(i) + message)
        send_message_button = driver.find_element(by='xpath', value='//button/span[text()="Send"]')
        send_message_button.click()
        time.sleep(1)
        print("Message Sent: " + str(i) )
        close_its_match_window = driver.find_element(by='xpath', value='//button[@title="Back to Tinder"]')
        close_its_match_window.click()

    except:
        try:
            hide_popup = driver.find_element(by='xpath', value='//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"] | //div[text()="Not interested"]/ancestor::button')
            hide_popup.click()
            print("Pop up closed!")

        except:
            try:
                cooldown_popup = driver.find_element(by='xpath', value='//button/span[text()="Close"]')
                driver.execute_script("arguments[0]?.click();", cooldown_popup)
                print("Max likes reached!")
                break

            except:
                pass

driver.close()
print("Site closed!")
driver.quit()
print("Browser closed!")

