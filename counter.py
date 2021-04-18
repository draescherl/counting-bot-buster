from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep


def element_exists(xpath):
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

    def get_starting_index(self):
        index = 47
        xpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[" + str(index) + "]/div[1]/div"
        while (element_exists(xpath)):
            index += 1
            xpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[" + str(index) + "]/div[1]/div"
        return index - 1

    def is_my_turn(self, index, i):
        new_index = index + 2
        xpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[" + str(new_index) + "]/div[1]/div"
        print('Searching for element ' + str(new_index))
        while (not element_exists(xpath)):
            continue
        print("Found content : " + str(self.driver.find_element_by_xpath(xpath).text))
        print("Comparing with : " + str(i))
        return self.driver.find_element_by_xpath(xpath).text == str(i)

    def count(self):
        broken = False
        i = 1 + self.offset
        # index = self.get_starting_index()

        while True:
            sleep(0.1)
            index = self.get_starting_index()
            if (i == 2):
                self.is_my_turn(index, i - 1)

            if broken:
                print("Count broken, restarting.")
                i = 1 + self.offset
                broken = False
            else:
                actions = ActionChains(self.driver)
                actions.send_keys(i)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                print("Wrote message : " + str(i))
                i += 2
                if (not self.is_my_turn(index, i - 1)):
                    broken = True
                    actions = ActionChains(self.driver)
                    actions.send_keys("T'es relou Dimitri...")
                    actions.send_keys(Keys.ENTER)
                    actions.perform()
                    sleep(5)


# offset = 0 -> odd numbers
# offset = 1 -> even numbers
bot = Bot(0)
bot.connect()
input('Hit enter when you are logged in and on the right channel')
bot.count()
