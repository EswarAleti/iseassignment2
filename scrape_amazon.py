from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
email = driver.find_element_by_id("ap_email")
email.send_keys("eswaraleti143@gmail.com")
signin = driver.find_element_by_id("continue")
signin.click()

pswd = driver.find_element_by_id("ap_password")
pswd.send_keys("amazon.com")
signin = driver.find_element_by_id("signInSubmit")
signin.click()

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("mobiles")
search.send_keys(Keys.ENTER)

mobiles=""
def get_mobiles():
	global mobiles
	for i in range(1,20):
		try:
			title = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div["+str(i)+"]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")
			mobiles+=title.text+'\n'
		except:
			pass

for page in range(1,5):
	if page>=2:
		try:
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/span[8]/div/span/div/div/ul/li[7]/a").click()
			get_mobiles()
		except:
			pass
	else:
		get_mobiles()

file = open("mobiles_amazon.txt","w")
file.write(mobiles)
file.close()