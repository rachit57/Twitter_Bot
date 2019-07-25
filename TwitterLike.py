#you need python,firefox and Gecko Driver 
from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class Twitter_Bot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()
	
	def login(self):
		bot = self.bot
		bot.get('https://twitter.com/')
		time.sleep(5)
		email = bot.find_element_by_class_name('email-input')
		password = bot.find_element_by_name('session[password]')
		email.clear()
		password.clear()
		email.send_keys(self_username)
		password.send_keys(self.password)
		password.send_keys(keys.RETURN)
		time.sleep(5)

	def like(self,hashtag):
		bot = self.bot
		bot.get('https://twitter.com/search?q=' + hashtag +&src=typeahead_click')
		time.sleep(5)
		for i in range(1,5)
		bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
		time.sleep(5)
		tweets = bot.find_elements_by_class_name('tweet')
		links = [elem.get_attribute('data-permalink-path') for elem in tweets]
		for link in links:
			bot.get('https://twitter.com/' + link)
			try:
				bot.find_element_by_class_name('HeartAnimation').click()
				time.sleep(30)
			except Exception as exp:
				time.sleep(60)

obj = Twitter-bot('Your_email_id','Your_password')
obj.login()
obj.like('a_hashtag')
