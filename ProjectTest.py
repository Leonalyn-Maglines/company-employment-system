from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class PageTest(unittest.TestCase):
	def setUp(self):
	    self.browser = webdriver.Firefox()

	def test_browser_title(self):
	    self.browser.get('http://localhost:8000/')
	    self.assertIn("Company Management System",self.browser.title)

	def check_for_rows_in_list_table(self,row_text):
	    table = self.browser.find_element_by_id('listTable')
	    rows = table.find_elements_by_tag_name('tr')
	    self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
	    self.browser.get('http://localhost:8000/')
	    self.assertIn("Company Management System",self.browser.title)

	    header_Text = self.browser.find_element_by_tag_name('h1')
	    self.assertIn("Company Management System", header_Text)
	 
	

	    Cname = self.browser.find_element_by_id('Cname')
	    self.assertEqual(Cname.get_attribute('placeholder'), "Cname")
	    inputCname.click()
	    inputCname.send_keys('iQor')
	    time.sleep(1)
	    
	    
	    inputDestablish = self.browser.find_element_by_id('Destablish')
	    inputDestablish.click()
	    inputDestablish.send_keys('08-24-2000')
	    time.sleep(1)
	  
	    inputCdescription = self.browser.find_element_by_id('Cdescription')
	    inputCdescription.click()
	    inputCdescription.send_keys('iQor is a managed services provider of customer engagement and technology-enabled BPO solutions.')
	    time.sleep(1)
	 
	    inputmission = self.browser.find_element_by_id('mission')
	    inputmission.click()
	    inputmission.send_keys('We support your customer wherever and whenever they need assistance.')
	    time.sleep(1)
	 
	    inputvision = self.browser.find_element_by_id('vision')
	    inputvision.click()
	    inputvision.send_keys('Making people happy is at the heart of what we do.')
	    time.sleep(1)

	    inputlocation = self.browser.find_element_by_id('location')
	    inputlocation.click()
	    inputlocation.send_keys('SM City Dasmarinas')
	    time.sleep(1)

	    inputCaddress = self.browser.find_element_by_id('Caddress')
	    inputCaddress.click()
	    inputCaddress.send_keys("3rd Floor SM City Dasmariñas, Governor's Dr, Barangay Sampaloc 1, Dasmariñas, 4114 Cavite")
	    time.sleep(1)

	    inputCnumber = self.browser.find_element_by_id('Cnumber')
	    inputCnumber.click()
	    inputCnumber.send_keys('0918-807-4225')
	    time.sleep(1)

	    btnProceed = self.browser.find_element_by_id('btnProceed')
	    btnProceed.click()
	    time.sleep(2)
	 


	
if __name__=='__main__':
	 	unittest.main()

''''	#this page should update and show two types of id on the list
	 Pet = self.browser.find_element_by_id('pet')
	 Pet.click()
	 time.sleep(1)
	 Pet.send_keys('Kuma')
	 time.sleep(1)
	 Breed = self.browser.find_element_by_id('breed')
	 Breed.click()
	 time.sleep(1)
	 Breed.send_keys('Pomeranian')
	 time.sleep(1)
	 Day = self.browser.find_element_by_id('birthday')
	 Day.click()
	 time.sleep(1)
	 Day.send_keys('05/25/2012')
	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)
	 #self.assertIn('1: Shana Puspin born on 08/22/2013',[row.text for row in rows])
	 #self.assertIn('1: Kuma Pomeranian born on 05/25/2012',[row.text for row in rows])
	 self.check_for_rows_in_list_table('1: Shana Puspin born on 08/22/2013')
	 self.check_for_rows_in_list_table("1: Kuma Pomeranian born on 05/25/2012")
	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_element_by_tag_name('tr')
'''
