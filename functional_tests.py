import unittest
from selenium import webdriver

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
        self.fail('Finish the test!') 
#He is invited to enter a to-do items straight away

# He types "Buy Chicken" into a text box (Everyone loves chicken)
if __name__ == '__main__':
    unittest.main()
# When he hits enter, the page updates and now the page lists:
# "1: Buy Chicken"

# There is still a text box inviting him to add another item. He enters
# "2: Cook the chicken tonight".

# Harry wonders whether or not the site will remember his list. Then he sees
# that the site has generated an unique URL for him -- there is some 
# explanatory text to that effect.

# He visits that URL - his to-do lists is still there.

# Satisfied, he goes back to sleep.


