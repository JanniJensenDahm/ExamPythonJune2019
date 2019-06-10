import unittest
import exam

class testMain(unittest.TestCase):

    #Returns true if filename is WebSacrape.md
    def testFile(self):
        exam.main()
        self.assertEqual(exam.mdFile, 'WebScrape.md')

    #Return true if method returns a dictionary
    def testDictionary(self):
        exam.main()
        self.assertTrue(isinstance(exam.aLinkOnSite(exam.htmlTextHome), dict))

if __name__ == '__main__':
    unittest.main(warnings='ignore')