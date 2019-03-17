from seleniumbase import BaseCase
import time
from selenium import webdriver

class TwitterTrendCapture(BaseCase):

    def slow_click(self, css_selector):
        time.sleep(1)
        self.click(css_selector)


    def is_in_loginpage(self):
        if self.is_element_present("input.js-username-field.email-input.js-initial-focus"):
            return True
        else:
            return False


    def test_twitter_trend_capture(self):

        self.open("https://twitter.com/login?lang=en")
        if self.is_in_loginpage() :
            self.update_text_value("input.js-username-field.email-input.js-initial-focus", "")
            self.update_text_value("input.js-password-field", "")
            self.slow_click("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")

        all_spans = self.driver.find_elements_by_xpath("//span[@class='u-linkComplex-target trend-name']")
        for span in all_spans:
            print(span.text)
        
        

            
        
        
        
