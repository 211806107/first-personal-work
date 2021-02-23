#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
path_txt='C:/Users/陈伟超/Desktop/第一次编程作业/1.txt'
f = open(path_txt,'rb').read()
default_mode =jieba.cut(f)
text = " ".join(default_mode)
background_image = np.array(Image.open("C:/Users/陈伟超/Desktop/第一次编程作业/t.png"))
stopwords = set(STOPWORDS)
stopwords.add("said")
wc = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",background_color="white",max_words=2000,mask=background_image,stopwords=stopwords)  
wc.generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(background_image, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
#plt.show()
wc.to_file('ciyun.png')
from IPython.display import Image
Image('ciyun.png')


# In[ ]:




