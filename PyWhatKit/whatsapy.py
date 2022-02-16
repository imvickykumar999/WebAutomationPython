
import pywhatkit

# Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+918239957923", "Hi", 00, 43)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+918239957923", "Hi", 00, 39, 15, True, 2)

# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("FOynWhcNPzX1WFMaUPiDcA", "Saboot_ss.jpg", "Hello, this photo is sent from Selenium library.")

# Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+918239957923", "Saboot_ss.jpg")

# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("FOynWhcNPzX1WFMaUPiDcA", "Hello, this photo is sent from Selenium library!", 0, 37)

# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("FOynWhcNPzX1WFMaUPiDcA", "Hey All!")

# ----------------------------------------------

# # Play a Video on YouTube
vid = 'JGwWNGJdvx8'
# pywhatkit.playonyt(vid)

from selenium import webdriver
import time

# web = webdriver.Chrome()
web = webdriver.Chrome(executable_path=r"chromedriver.exe")

web.get(f'https://www.youtube.com/watch?v={vid}')
time.sleep(5)

# play = web.find_element_by_xpath('//*[@id="movie_player"]/div[25]/div[2]/div[1]/button')
# play.click()

# adds_stop = web.find_element_by_xpath('//*[@id="ad-text:6"]')
# adds_stop.click()