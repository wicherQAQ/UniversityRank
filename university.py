from bs4 import BeautifulSoup

htmlfile = open("./university.html", 'r', encoding='utf-8')
soup = BeautifulSoup(htmlfile.read(), 'html.parser')

#查询大学的数量
universityAmount = 500

universityList = soup.find_all("div", class_="item-right",limit=universityAmount)

list=[]


for index,item in enumerate(universityList):
	name = item.find_all("p",class_="item-name")[0].string
	location = item.find_all("p",class_="item-location")[0].string
	university = {"rank":index+1,"name":name,"location":location}
	tagList = []
	for subItem in item.find_all('div',class_="tag-text"):
		tag = subItem.string.replace(" ","").replace("\n","")
		tagList.append(tag)
	university['tagList'] = tagList
	list.append(university)


name = input("学校全名:")

for index,item in enumerate(list):
	if name == item["name"]:
		print(item)
		break

#print(list)


# fout = open("./rank.txt", "w")

# for item in list:
# 	info = str(item['rank'])+'--'+str(item['name'])+'--'+str(item['location'])
# 	sep = "#";
# 	tags = sep.join(item['tagList'])
# 	fout.write(info+'==='+tags+'\n')



# 	# for tag in item['tagList']:
# 	# 	fout.write(tag+'--')
# 	# fout.write("\n")
    

# fout.close()

	
