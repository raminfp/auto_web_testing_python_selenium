import unittest
from testAll import TestAbout
from testAll import TestHome

#https://stackoverflow.com/a/12011486
def suite():

    # Home page test
    suite = unittest.TestSuite()
    suite.addTest(TestHome('test_TC001_python_docs_button'))
    suite.addTest(TestHome('test_TC0002_search_python_org'))

    ## About page test
    suite.addTest(TestAbout('test_TC003_about_page'))

    ## Contact_Us page test

    ## Dashboard page test
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite_var = suite()
    runner.run(suite_var)
