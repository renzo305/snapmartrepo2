from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import *
import time
import random


class Keywords:
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe", options=self.options)


    def inputText(self, fieldXpath, fieldValue = ""):
        time.sleep(5)
        self.driver.find_element_by_xpath(fieldXpath).send_keys(fieldValue)

    def clickBtn(self, fieldXpath):

        self.driver.find_element_by_xpath((fieldXpath)).location_once_scrolled_into_view
        time.sleep(4)
        self.driver.find_element_by_xpath(fieldXpath).click()
        time.sleep(5)

    def clickRadioBtn(self,fieldXpath, listValues):
        randomChoice = random.choice(listValues)
        newFieldXpath = fieldXpath.format(randomChoice)
        self.driver.find_element_by_xpath((newFieldXpath)).location_once_scrolled_into_view
        time.sleep(2)
        self.driver.find_element_by_xpath(newFieldXpath).click()
        time.sleep(3)

    def checkElementPresence(self, fieldXpath):
        time.sleep(2)
        self.driver.find_elements_by_xpath(fieldXpath)

    def chooseRandomElement(self, fieldXpath, descendants="", valCount=0):
        self.driver.find_elements_by_xpath(fieldXpath)
        countElement = len(self.driver.find_elements_by_xpath(fieldXpath))

        counter = valCount
        while counter != 0:
            try:
                randomClick = random.randint(1, countElement)
                chosenValue = fieldXpath + descendants.format(randomClick)
                time.sleep(2)
                chosenElement = self.driver.find_element_by_xpath(chosenValue)
                chosenElement.location_once_scrolled_into_view
                time.sleep(3)
                chosenElement.click()
                counter -= 1

            except:
                pass

        chosenElement.send_keys(Keys.HOME)
        self.driver.execute_script("window.scrollTo(0, 0);")

    def takeScreen(self, testname):
        now = datetime.now()
        now_str = str(now)

        # Removing special characters that are not accepted in saving a file
        now_str = now_str.replace(":", "_")
        now_str.replace(".", "_")
        time.sleep(4)
        # Saving the file using concatenated date and time string
        self.driver.save_screenshot(
            './TestEvidence/' + testname + '_' + now_str + '.' + "png")


    def scrollUp(self, fieldXpath):
        self.driver.find_element_by_xpath(fieldXpath).send_keys(Keys.HOME)
        time.sleep(3)

    def scrollDown(self):
        self.driver.find_element_by_xpath("").send_keys(Keys.END)