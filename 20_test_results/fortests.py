import unittest


class TestExample(unittest.TestCase):

    def test_example_1(self):
        self.assertTrue(True)

    def test_example_2(self):
        self.assertFalse(False, 'Example of failed test case')

    @unittest.skip('please skip this function')
    def test_example_3(self):
        self.assertTrue(True)


def suite():
    suite_ = unittest.TestSuite()
    suite_.addTest(TestExample('test_example_1'))
    suite_.addTest(TestExample('test_example_2'))
    suite_.addTest(TestExample('test_example_3'))
    return suite_


if __name__ == "__main__":
    result = unittest.TextTestRunner().run(suite())
