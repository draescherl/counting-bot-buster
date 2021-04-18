from selenium import webdriver

from time import sleep

class Bot():
    def __init__(self, offset):
        self.driver = webdriver.Firefox()
        self.offset = offset
    
    def connect(self):
        self.driver.get('https://discord.com/channels/819626874035503204/819974354955141141')
        sleep(3)


    def count(self):
        inputArea = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]/div/span/span/span')
        self.driver.execute_script("arguments[0].innerText = 'test'", inputArea)


bot = Bot(0)
bot.connect()
input('Hit enter when you are logged in and on the right channel')
bot.count()