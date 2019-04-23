
# coding: utf-8

# In[19]:

import os
def print_directory_contents(sPath):                                     
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
            
sPath = "/Users/avinashbarnwal/Desktop/Course"            
print_directory_contents(sPath)            

