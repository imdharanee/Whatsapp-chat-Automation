import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
driver=webdriver.Chrome()
baseurl="https://web.whatsapp.com"

driver.get(baseurl)
time.sleep(10)

with open("mymessage.csv",newline='') as csvfile:          #csv file that contains the phone number and the message that are to be sent to that particular contact.
                                                           #can add multiple contacts and messages.
    readContacts = csv.reader(csvfile)
    for phone,msg in readContacts:
        phonenum= phone
        message= msg

        sameTab= (baseurl+ "/send?phone=" + str(phonenum))

        driver.get(sameTab)

        time.sleep(27) #depends on your internet speed and refresh rate                                 
        #time for selenium to wait..to move on to the next step,(i.e,after scanning qr code,no.of seconds,that it has to wait)
         
        content= driver.switch_to.active_element
        content.send_keys(message)

        content.send_keys(Keys.RETURN)

        time.sleep(25)              #time for the software to wait for quiting after sending the message.


