import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
# Harry has a lot to do, and he has found the perfect to-do app to do it with.
# He goes to check out its homepage
        self.browser.get('http://localhost:8000')
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

# There is still a text box inviting him to add another item. He enters
# "2: Cook the chicken tonight".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Cook the chicken tonight')
        inputbox.send_keys(Keys.ENTER)

#The page updates again, and now shows both items on the list

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy chicken', [row.text for row in rows])
        self.assertIn('2: Cook the chicken tonight', 
                      [row.text for row in rows])

        self.fail('Finish the test!')
# Harry wonders whether or not the site will remember his list. Then he sees
# that the site has generated an unique URL for him -- there is some 
# explanatory text to that effect.

# He visits that URL - his to-do lists is still there.

# Satisfied, he goes back to sleep.

if __name__ == '__main__':
    unittest.main()
