try:
	import requests  ,re, os , sys , random , uuid , user_agent , json,secrets
	from uuid import uuid4
	from user_agent import generate_user_agent
	
except ImportError:
	os.system('pip install requests')
	os.system('pip install user_agent')
	
class salammzere3:
	
	def Instalogin(email,password):
		
		UrlSalam = 'https://www.instagram.com/accounts/login/ajax/'
		
		HeadSalam = {

    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-length':'317',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'mid=YdduAwAEAAH5tvQgBxaWFmtCauW1; ig_did=3B9E189F-664C-4C27-BAD4-A4DC839FFFFA; ig_nrcb=1; shbid="15789\0545722116218\0541674148260:01f7b34891a790ddc3b2f8f61b0c76d2e539c3efaedb09b6812283940bfcc6739f7a6930"; shbts="1642612260\0545722116218\0541674148260:01f74a3f9c5b7857cd36ad8a36a61bbe4bcc22061a61a730590ea1f665bd85916ae193b4"; csrftoken=qMiGRabzXyZlJPciGxtTKQAJZkCv0Rhi',
    'origin':'https://www.instagram.com',
    'referer':'https://www.instagram.com/',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':generate_user_agent(),
    'x-asbd-id':'198387',
    'x-csrftoken':'qMiGRabzXyZlJPciGxtTKQAJZkCv0Rhi',
    'x-ig-app-id':'936619743392459',
    'x-ig-www-claim':'0',
    'x-instagram-ajax':'9e76603e49dc',
    'x-requested-with':'XMLHttpRequest'}
    
		DatSalam = {
	'username': email,
	'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+ password
	}
		ReqSalam = requests.post(UrlSalam,headers=HeadSalam,data=DatSalam)
		if ('"authenticated":true') in ReqSalam.text:
			
			
			os.system('rm -rf sessionid.txt')
			
			APK = ReqSalam.cookies['sessionid']
			
			f = open('sessionid.txt','a')
			
			f.write(APK+"\n")
			
			f.close()
			
			return True
			
		if str('"message":"challenge_required","challenge"') in ReqSalam.text:
			
			return False
			
		else:
			
			return None
		
