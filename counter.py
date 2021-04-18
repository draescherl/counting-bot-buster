from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep

def isElementHere(xpath):
    try:
        bot.driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


class Bot():
    def __init__(self, offset):
        self.driver = webdriver.Firefox()
        self.offset = offset
    
    def connect(self):
        self.driver.get('https://discord.com/channels/819626874035503204/819974354955141141')
        sleep(3)

# /html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[52]/div[1]/div
# /html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[53]/div[1]/div

    def get_index(self):
        index = 47
        xpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[" + str(index) + "]/div[1]/div"
        while (isElementHere(xpath)):
            index += 1
            xpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[" + str(index) + "]/div[1]/div"
        return index - 1

    def is_my_turn(self, index, i):
        xpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[" + str(index + i) + "]/div[1]/div"
        print('searching for element ' + str(index + i))
        while (not isElementHere(xpath)):
            print('here')
            continue

        return self.driver.find_element_by_xpath(xpath).text == str(i - 1)


    def count(self):
        inputArea = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]/div')
        inputArea.click()
        broken = False
        while not broken:
            broken = False
            i = 1 + self.offset
            index = self.get_index()
            print("index :" + str(index))
            print("i :" + str(i))
            while not broken:
                actions = ActionChains(self.driver)
                actions.send_keys(i)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                i += 2
                if (self.is_my_turn(index, i)):
                    continue
                else:
                    broken = True
                    # actions = ActionChains(self.driver)
                    # actions.send_keys("T'es relou Dimitri...")
                    # actions.send_keys(Keys.ENTER)
                    # actions.perform()
                sleep(1)



# ca casse => 53
# 1 => 54
# wait for 55
# check if 55 == i-1



# offset = 0 -> odd numbers
# offset = 1 -> even numbers
bot = Bot(0)
bot.connect()
input('Hit enter when you are logged in and on the right channel')
bot.count()