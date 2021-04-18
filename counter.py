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
        xpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[" + str(index + i) + "]/div[1]/div"
        # print('searching for element ' + str(index + i))
        while (not element_exists(xpath)):
            continue
        # print(self.driver.find_element_by_xpath(xpath).text)
        # print(i)
        return self.driver.find_element_by_xpath(xpath).text == str(i)

    def count(self):
        inputArea = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]/div')
        inputArea.click()
        broken = False
        i = 1 + self.offset
        index = self.get_starting_index()

        # print("i : " + str(i))
        # print("start index : " + str(index))
        while True:
            sleep(1)
            if (i == 2):
                self.is_my_turn(index, i - 1)

            if broken:
                # print("Count broken, restarting.")
                i = 1 + self.offset
                index = self.get_starting_index()
                broken = False
            else:
                actions = ActionChains(self.driver)
                actions.send_keys(i)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                # print("Wrote message")
                i += 2
                # print("New i : " + str(i))
                if (not self.is_my_turn(index, i - 1)):
                    broken = True
                    actions = ActionChains(self.driver)
                    actions.send_keys("T'es relou Dimitri...")
                    actions.send_keys(Keys.ENTER)
                    actions.perform()
                    sleep(3)


# offset = 0 -> odd numbers
# offset = 1 -> even numbers
bot = Bot(1)
bot.connect()
input('Hit enter when you are logged in and on the right channel')
bot.count()
