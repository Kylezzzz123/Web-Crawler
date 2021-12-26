import requests
import re
# The first web crawler
# send a request
url = 'https://www.qiushibaike.com/video/'

# hearders is to anti-inspection, pretent to be a web browser 
hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
resp = requests.get(url, headers=hearders)

# first parameter is protocol, the second parameter is content; .*  is anything after the .  ,  r is original string
info = re.findall(r'<source src="(.*)" type=\'video/mp4\' />', resp.text)
#print(resp.text)
#print(info)

# print(type(info))   # output: type is list
lst = []
for item in info:
    lst.append('http:' + item)
# print(lst)        # got all the video links


# download vidoes
count = 0  # for naming vidoes
for item in lst:
    #request
    resp = requests.get(item, headers=hearders)  #get the video links
    count+=1
    with open('video/'+str(count)+'.mp4', 'wb') as file:    # wb is binary write, write the vidoes into local drive
        file.write(resp.content)       # because video is binary data, so we use resp.content, not resp.text
print("Videos download completed")