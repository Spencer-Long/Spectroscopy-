# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
from astropy.io import fits
from astropy import units as u


# In[2]:


hdul = fits.open('/Users/Spencer/Desktop/Spectroscopy320/Spectra_Data/4.ELG.fits')


# In[8]:


manual = hdul[0].header # Assgining variable to call header data of fits file


# In[9]:


data = hdul[0].data # Storing Flux density data into memory (will be used for our y axis)


# In[34]:


plt.figure(figsize=(15,5))
plt.xlim(data[0],len(data))
plt.ylim(-.7e-18,9.5e-18)
plt.plot(data) # Plotting flux data to take a quick look. 


# In[35]:


wave = ['3726','3728','3797','3835','3868','3889','3933','3968','3970','4101','4340.5','4861','4958.8','5006.8','5875.6','6548','6562.8','6583.4','6716.5','6730','7135','9068','9530']
symbol = ['[O II]','[O II]','H10','H9','[Ne III]','H8','H','K','H7',r'$H\delta$',r'$H\gamma$',r'$H\beta$','[O III]','[O III]','He I','[N II]','H-Alpha','[N II]','[S II]','[S II]','[Ar III]','[S III]','[S III]']


# In[60]:


manual


# In[38]:


x = np.arange(7598.57,len(data)*2.553+7598.57,2.553) # first method 

x = np.arange(manual['CRVAL1'], len(data) * manual['CDELT1'] + manual['CRVAL1'], manual['CDELT1']) # second method

data.shape == x.shape # This line of code verifies that the x axis array is the same shape as the y axis array.


# In[59]:


# Taking a look after creating x axis with correct wavelength data from manual

plt.figure(figsize=(15,5))
#plt.xlim(data[0],len(data))
plt.ylim(-.7e-18,9.5e-18)
plt.plot(x,data) # Plotting flux data to take a quick look.
plt.show()


# In[44]:


# Balmer line labels for plots and dataframe
balmer_lines = [ 
                r'$H\beta$',
                r'$H\gamma$',
                r'$H\delta$',
                r'$H\epsilon$',
                r'$H8$',
                r'$H9$'
               ]

# Wavelengths for Balmer lines
wl = [
      4861.33,
      4340.47,
      4101.74,
      3970.07,
      3889.05,
      3835.39
     ]  


# In[46]:


# Calculates the current wavelength of the line in question

def doppler_wavelength(wavelength_rest, velocity):
    
    vel = velocity * u.kilometer*u.second**-1
    speed_light = 299792.458*u.kilometer*u.second**-1 # Speed of light (Source: Comptes Rendus de la 17e CGPM (1983), 1984, p.97)
    lamda_rest = wavelength_rest * u.angstrom # rest wave length of line in question
    
    lambda_shift = ((vel / speed_light) +1) * lamda_rest
    
    return lambda_shift


# In[47]:


# Calculates the overall shift due to the doppler effect

def doppler_shift(rest_wavelength, current_wavelength):
    
    shift = abs(rest_wavelength - current_wavelength)
    
    return shift


# In[56]:


# Calculates the velocity of the object in question

def doppler_velocity(lambda_rest, lambda_shift):
    
    speed_light = 299792.458*u.kilometer*u.second**-1 # Speed of light in km/s (Source: Comptes Rendus de la 17e CGPM (1983), 1984, p.97) 
    lr = lambda_rest * u.angstrom # lab tested wavelength
    ls = lambda_shift * u.angstrom # wavelength that the line is currently located
    velocity = ((ls -lr) / (lr)) * speed_light
    
    return velocity  

