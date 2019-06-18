import unittest
import exam
from unittest.mock import patch
import os

class testMain(unittest.TestCase):

    #Run program
    def setUp(self):
        exam.main()
        self.url = 'https://clbokea.github.io/exam/index.html'

    #Returns true if filename is WebSacrape.md
    def test_file(self):
        self.assertTrue(os.path.isfile('./WebScrape.md'))
        
    #Return true if method returns a dictionary
    def test_dictionary(self):
        self.assertTrue(isinstance(exam.aLinkOnSite(exam.htmlTextHome), dict))

    #Return true if method returns a list
    def test_list(self):
        self.assertTrue(isinstance(exam.h1TagOnSite(exam.htmlTextHome), list))

    #Return true if method returns len(list) = 4
    def test_list_length(self):
        self.assertEqual(4, len(exam.imageOnSite(exam.urlList)))
    
    #Test connection
    def test_url_connection(self):
        with patch('exam.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            connection = exam.url_connection(self.url)
            self.assertEqual(connection, 'Success')
            
            mocked_get.return_value.ok = False
            connection = exam.url_connection(self.url)
            self.assertEqual(connection, 'Bad Response!')
            

if __name__ == '__main__':
    unittest.main(warnings='ignore')
