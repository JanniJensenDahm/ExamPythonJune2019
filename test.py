import unittest
import exam

class testMain(unittest.TestCase):

    #Run program
    exam.main()

    #Returns true if filename is WebSacrape.md
    def testFile(self):
        self.assertEqual(exam.mdFile, 'WebScrape.md')

    #Return true if method returns a dictionary
    def testDictionary(self):
        self.assertTrue(isinstance(exam.aLinkOnSite(exam.htmlTextHome), dict))

    #Return true if method returns a list
    def testList(self):
        self.assertTrue(isinstance(exam.h1TagOnSite(exam.htmlTextHome), list))

    #Return true if method returns len(list) = 4
    def testListLength(self):
        self.assertEqual(4, len(exam.imageOnSite(exam.urlList)))
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')