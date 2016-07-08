# Lofter用户相册爬取
# 提供用户主页地址，爬取该用户发布的所有图片

import os, time
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

headers = {
	'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language' : 'zh-CN,zh;q=0.8',
}

# url = "http://piadiary.lofter.com/"	# web home url 
url = input("input user's home url(like 'http://somebody.lofter.com/'):")
dir_name = input("diretory name:")
endPage = int(input("pages:"))
dir_img = "D:\photos\\" + dir_name
print(dir_img)

req = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(req)
the_page = response.read()

count = 0
url_imgs = []
if not os.path.exists(dir_img):
	os.makedirs(dir_img)
print("Begin")
print("get all images url...")

for x in range(1,endPage):
	pageUrl = url + "?page=" + str(x)
	req = urllib.request.Request(pageUrl, None, headers)
	response = urllib.request.urlopen(req)
	page = response.read()
	soup = BeautifulSoup(page, "html.parser")
	# "m-post m-post-img    masonry-brick"
	# bigimgsrc
	for iterm in soup(class_ = "img"):
		post_url = ''
		try:
			post_url = iterm['href']
		except:
			post_url = iterm.a['href']
		try:
			req = urllib.request.Request(post_url, None, headers)
			response = urllib.request.urlopen(req)
			page = response.read()
			soup = BeautifulSoup(page, "html.parser")
			bgImg_1 = soup(class_='imgclasstag')
			bgImg_2 = soup(class_='img imgclasstag')
			url_img = ''
			if bgImg_1:
				url_img = bgImg_1[0]['bigimgsrc']
			elif bgImg_2:
				url_img = bgImg_2[0]['bigimgsrc']
			else:
				pass
			url_imgs.append((url_img, count))
			# text_urls.write(url_img + "\n")
			count = count + 1
		except:
			pass
print("done.")
print("download...")
def download(url):
	urllib.request.urlretrieve(url[0], dir_img + "\\" + str(url[1]) + ".jpg")
	print(url[1])
	url_imgs.remove(url)
	# url_imgs 列表中删除确定下载完成的，将没有完成的存到...

page_pool = ThreadPool(6)
page_pool.map(download, url_imgs)
page_pool.close()
page_pool.join()

text_urls = open("dir_img" + "\\text_urls.txt", "w")
for i in url_imgs:
	text_urls.write(i[1] + "\n")
print("done.")