#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import re
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'    
}
frontalPart = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor="
latterPart= "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_="
Cursor = "0"
num = 1613958004052
total = 0
with open('TencentVideoReview.txt','a',encoding = 'utf-8') as file:
        file.write("评论过多，只获取前10000条左右的评论\n")
while(total < 10000):
    url = frontalPart + Cursor + latterPart + str(num)
    num += 1
    res=requests.get(url,headers=headers)
    Cursor = re.findall('"last":"(.*?)","hasnext"',res.text)[0]
    content = re.findall('"content":"(.*?)","up"',res.text)
    for i in range(len(content)):
        with open("TencentVideoReview.txt","a",encoding = 'utf-8') as file:
            file.write(content[i] + "\n")
    total = total + i + 1
page -= 1
with open("TencentVideoReview.txt","a",encoding = 'utf-8') as file:
    file.write("评论共计 " + str(total) + " 条")


# In[ ]:




