import requests
import time
from dhooks import Webhook, Embed


#hook keys
gonehook = Webhook('WEBHOOK HERE')
realgirlshook = Webhook('WEBHOOK HERE')
spreadhook = Webhook('WEBHOOK HERE')
facedownhook = Webhook('WEBHOOK HERE')


#Scrape the subreddit
subreddit = 'nsfw'
user_agent = 'Reddit JSON API teaching example/1.0'
num_limit = 1000

gonewilds = requests.get('https://www.reddit.com/r/gonewild/.json?limit={}'.format(subreddit, num_limit),
            headers={'User-Agent': user_agent}).json()
			
for gonewild in gonewilds['data']['children']:
	suhdude1 = ('{gonewild[url]:40}'.format(gonewild=gonewild['data']))
	gonewildtitle = ('{gonewild[title]}'.format(gonewild=gonewild['data']))
	embed1 = Embed(
			description=gonewildtitle,
			color=0x1e0f3,
			timestamp='now'  # sets the timestamp to current time
			)
	image1 = suhdude1
	embed1.set_image(image1)

	gonehook.send(embed=embed1)
	
time.sleep(3)
	
realgirls = requests.get('https://www.reddit.com/r/realgirls/.json?limit={}'.format(subreddit, num_limit),
            headers={'User-Agent': user_agent}).json()
			
for realgirl in realgirls['data']['children']:
	suhdude3 = ('{realgirl[url]:40}'.format(realgirl=realgirl['data']))
	realgirltitle = ('{realgirl[title]}'.format(realgirl=realgirl['data']))
	embed3 = Embed(
			description=realgirltitle,
			color=0x1e0f3,
			timestamp='now'  # sets the timestamp to current time
			)
	image3 = suhdude3
	embed3.set_image(image3)

	realgirlshook.send(embed=embed3)
	
time.sleep(3)
	
spreadems = requests.get('https://www.reddit.com/r/spreadem/.json?limit={}'.format(subreddit, num_limit),
            headers={'User-Agent': user_agent}).json()
			
for spreadem in spreadems['data']['children']:
	suhdude4 = ('{spreadem[url]:40}'.format(spreadem=spreadem['data']))
	spreademtitle = ('{spreadem[title]}'.format(spreadem=spreadem['data']))
	embed4 = Embed(
			description=spreademtitle,
			color=0x1e0f3,
			timestamp='now'  # sets the timestamp to current time
			)
	image4 = suhdude4
	embed4.set_image(image4)

	spreadhook.send(embed=embed4)
	
time.sleep(3)
	
facedowns = requests.get('https://www.reddit.com/r/facedownassup/.json?limit={}'.format(subreddit, num_limit),
            headers={'User-Agent': user_agent}).json()
			
for facedown in facedowns['data']['children']:
	suhdude5 = ('{facedown[url]:40}'.format(facedown=facedown['data']))
	facedowntitle = ('{facedown[title]}'.format(facedown=facedown['data']))
	embed5 = Embed(
			description=facedowntitle,
			color=0x1e0f3,
			timestamp='now'  # sets the timestamp to current time
			)
	image5 = suhdude5
	embed5.set_image(image5)

	facedownhook.send(embed=embed5)