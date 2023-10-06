#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import clipboard
import json


#Name of the json file where data will be stored
saved_data = "clipboard.json"

#defining the function to save the data to a file as key, value pairs
def save_data(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data,f)
        
        
#defining a function to read abd return the data as dictionary
def load_data(filepath):
    #executing a try statement if filepath(saved_data) doesn't exist
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}


#program will only take one command, therefore checking for how many commands user passed
if len(sys.argv)==2:# 2 because one being the name of the python file and other being the comman
    command=sys.argv[1]
    data = load_data(saved_data)
    
    
    #the conditional statement for respective commands
    if command.lower()=="save":
        key=input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(saved_data, data)
        print("Data Saved")
        
    
    
    elif command.lower()=="load":
        key=input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist.")
        
    
    elif command.lower()=="list":
        print(data)
    
    
    elif command.lower()=="delete":
        key=input("Enter a key: ")
        del data[key]
        save_data(saved_data, data)
        print('Key deleted')
    
    
    else:
        print("Unknown command")
else:
    print('Please pass exactly one command.')


# In[9]:





# In[ ]:




