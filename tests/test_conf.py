import unittest
from conf import WooCommerce

class TestWooCommerce(unittest.TestCase):

    def setUp(self):
        print("⚡ setUp ⚡")
        self.wc1 = WooCommerce()
        self.wc2 = WooCommerce()

    def test_get_key_value(self):
        print("⚡ check key value ⚡")       
        self.wc1.cunsumer_key = 123
        self.assertEqual(self.wc1.get_key(), 'The key must not numerical value')
 
        self.wc1.cunsumer_key = 'cfddfdsf'
        self.assertEqual(self.wc1.get_key(), 'The key starts with ck')
    
        self.wc1.cunsumer_key = 'ck_xxxxxxxxxxxxx'
        self.assertEqual(self.wc1.get_key(), 'The key is too short')


    def test_get_secret_value(self):
        print("⚡ check secret value ⚡")
        self.wc2.consumer_secret = 123       
        self.assertEqual(self.wc2.get_secret(), 'The secret must not numerical value')

        self.wc2.consumer_secret = 'cfddfdjiisf'
        self.assertEqual(self.wc2.get_secret(), 'The secret starts with cs')

        self.wc2.consumer_secret = 'cs_xxxxxxxxxxxxx'
        self.assertEqual(self.wc2.get_secret(), 'The secret is too short')

if __name__ == '__main__':
    print("🐍 run tests from TestWooCommerce 🐍")
    unittest.main()