#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import random 
from skimage import exposure 
from skimage.util import random_noise 
from skimage import transform 
from cv2 import resize


# In[6]:


img=mpimg.imread('puppy.jpg')
plt.imshow(img) 
img_rescale=resize(img, (500,700)) 
plt.imshow(img_rescale)


# In[18]:


horiz = np. fliplr(img_rescale) 
plt.imshow(horiz)


# In[11]:


vert = np.flipud(img_rescale) 
plt. imshow(vert)


# In[14]:


#rotation
from skimage import transform 
trans = transform.rotate(img_rescale, random.uniform(-50,50)) 
plt.imshow(trans)


# In[16]:


#random noise 
img_nos= random_noise(img_rescale, mode='s&p', clip=True) 
plt.imshow(img_nos)


# In[ ]:




