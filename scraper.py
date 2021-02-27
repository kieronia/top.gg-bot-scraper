import requests,time,os
pagenumber = 0
botsfound = 0
while True:
	pagenumber += 1
	data = requests.get(f"https://top.gg/list/top?page={pagenumber}")
	for line in data.text.split():
		if 'href="/bot/' in line:
			if len(line) == 30:
				botid = line.replace('href="/bot/',"").replace('"',"")			
				botinvite = f"https://discord.com/oauth2/authorize?client_id={botid}&permissions=8&scope=bot"
				print(botinvite)
				f = open("bots.txt","a")
				f.write(f"{botinvite}\n")
				botsfound += 1
				os.system(f"title On page {pagenumber} // Bots scraped : {botsfound}")


