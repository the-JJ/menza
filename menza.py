import requests
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

url = 'http://www.cassandra.hr/menu/studentski-menu/'
r = requests.get(url)

parsed_html = BeautifulSoup(r.text, "lxml")

menu = parsed_html.body.find('div', attrs={'class':'entry'}).text

# Remove empty line
menu = menu[1:]

# Remove vege menu
vege = 'MENU  3'

ind = menu.find(vege)
menu = menu[:ind-1]

def boldMenu(menu):
	startBold = '\033[1m'
	endBold = '\033[0m'

	menuList = menu.split('\n')
	newMenu = ''
	for x in menuList:
		if (x.startswith("MENU")):
			x = '\n' + startBold + x + endBold
		newMenu += x + '\n'
	return newMenu[:-1]

print(boldMenu(menu))