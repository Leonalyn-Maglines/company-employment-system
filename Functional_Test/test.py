from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class Compay_Management_System(LiveServerTestCase):



	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('id_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  
                   
                 
	def setUp(self):
	 self.browser = webdriver.Firefox()
	def test_Compay_Management_System(self):
	 self.browser.get('http://localhost:8000/')
	 
	 self.assertIn('Company',self.browser.title)
	 #header_text = self.browser.find_element_by_tag_name('h1').text
	 #self.assertIn('Company Management System', header_text)
	 Cname = self.browser.find_element_by_id('Cname')
	 self.assertEqual(Cname.get_attribute('placeholder'),'Enter your Company name')
	 Cname.click()
	 time.sleep(1)
	 Cname.send_keys('iQor')
	 time.sleep(1)
	 Destablish = self.browser.find_element_by_id('Destablish')
	 self.assertEqual(Destablish.get_attribute('placeholder'),"dd/mm/yyyy")
	 Destablish.click()
	 time.sleep(1)
	 Destablish.send_keys('08-24-2000')
	 time.sleep(1)

	 Cdescrption = self.browser.find_element_by_id('Cdescription')
	 self.assertEqual(Cdescrption.get_attribute('placeholder'),'Enter a company description')
	 Cdescrption.click()
	 time.sleep(1)
	 Cdescrption.send_keys('iQor is a managed services provider of customer engagement and technology-enabled BPO solutions.')
	 time.sleep(1)

	 mission = self.browser.find_element_by_id('mission')
	 self.assertEqual(mission.get_attribute('placeholder'),'Mission of company')
	 mission.click()
	 time.sleep(1)
	 mission.send_keys('We support your customer wherever and whenever they need assistance.')
	 time.sleep(1)

	 vision = self.browser.find_element_by_id('vision')
	 self.assertEqual(vision.get_attribute('placeholder'),'Vision of company')
	 vision.click()
	 time.sleep(1)
	 vision.send_keys('Making people happy is at the heart of what we do.')
	 time.sleep(1)

	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)


	 location = self.browser.find_element_by_id('location')
	 self.assertEqual(location.get_attribute('placeholder'),'Company branch')
	 location.click()
	 time.sleep(1)
	 location.send_keys('SM City Dasmarinas')
	 time.sleep(1)

	 Caddress= self.browser.find_element_by_id('Caddress')
	 self.assertEqual(Caddress.get_attribute('placeholder'),'Enter the full company address')
	 Caddress.click()
	 time.sleep(1)
	 Caddress.send_keys("3rd Floor SM City Dasmariñas, Governor's Dr, Barangay Sampaloc 1, Dasmariñas, 4114 Cavite")
	 time.sleep(1)


	 Cnumber = self.browser.find_element_by_id('Cnumber')
	 self.assertEqual(Cnumber.get_attribute('placeholder'),'Enter the contact number of company')
	 Cnumber.click()
	 time.sleep(1)
	 Cnumber.send_keys('0918-807-4225')
	 time.sleep(1)

	 btnNext = self.browser.find_element_by_id('btnNext')
	 btnNext.click()
	 time.sleep(2)
