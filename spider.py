import urllib2, urllib
import os
import BeautifulSoup

headers = {
	'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language' : 'zh-CN,zh;q=0.8',
}

url = "******"	# web home url 

count = 0
print "Begin"

for x in xrange(1,5):	
	pageUrl = url + str(x)	# every page url
	page = urllib2.Request(pageUrl, None, headers)
	page = urllib2.urlopen(page).read()

	soup = BeautifulSoup.BeautifulSoup(page)
	post = soup.findAll("div", "m-post m-post-photo")	# get the content where you need
	print "=============" + str(x) + "==============="
	for i in post:
		postUrl = i.find("div", "img").a['href']	# get post url 
		post_page = urllib2.Request(postUrl, None, headers)
		post_page = urllib2.urlopen(post_page).read()
		soup = BeautifulSoup.BeautifulSoup(post_page)
		soup = soup.find("div", "cont")
		soup = soup.findAll("div", "img")
		for i in soup:
			imageUrl = i.a["bigimgsrc"]
			if imageUrl :
				pass
			else:
				imageUrl = i.img["src"]
			print count
			urllib.urlretrieve(imageUrl,'%s.jpg' % str(count))		# download the image
			count = count + 1