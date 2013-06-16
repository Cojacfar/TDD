from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
# Harry has a lot to do, and he has found the perfect to-do app to do it with.
# He goes to check out its homepage
        self.browser.get(self.live_server_url)
#He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
#He is invited to enter a to-do items straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
# He types "Buy Chicken" into a text box (Everyone loves chicken)
      
        inputbox.send_keys('Buy chicken')
# When he hits enter, the page updates and now the page lists:
# "1: Buy Chicken"
        inputbox.send_keys(Keys.ENTER)
        harry_list_url = self.browser.current_url
        self.assertRegexpMatches(harry_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy chicken')

# There is still a text box inviting him to add another item. He enters
# "2: Cook the chicken tonight".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Cook the chicken tonight')
        inputbox.send_keys(Keys.ENTER)

#The page updates again, and now shows both items on the list
        
        self.check_for_row_in_list_table('2: Cook the chicken tonight')
        self.check_for_row_in_list_table('1: Buy chicken')

        #Now a new user, Francis, comes along to the site
        self.browser.quit()
        ##We use a new browser session to make sure that no information
        ##of Harry's is coming through from cookies ,etc.
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy chicken', page_text)
        self.assertNotIn('cook', page_text)

        #Francis starts a new list by entering a new item, He
        # is less interesting than Harry...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, harry_list_url)

        #Again, there is no trace of Harry's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy chicken', page_text)
        self.assertIn('Buy milk', page_text)
# Satisfied, he goes back to sleep.
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

