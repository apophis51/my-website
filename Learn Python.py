def sample_dictionary(): ####### This method initializes a sample dectionary
    blogs = {
        "vape pens" : "how to clean a vape pen",
        "bongs" : "how do bongs work",
        "bong types" : ["straight-tube","beaker","tall"],
        "keywords" : ["pretty", "big", "nice", "cool"]
    }
    return blogs

def dictionarycommands():
    my_dictionary = sample_dictionary()

    my_dictionary["bong types"].append("nice")  #### add a key to the dictionary
    print("this key has an appended value: ",  my_dictionary["bong types"])

    my_dictionary["bongs"]
    my_dictionary["bongs"] = [my_dictionary["bongs"]] ### converts key to a list so i can append
    my_dictionary["bongs"].append("this is cool")

    print("my list got appended with 'this is cool':", my_dictionary["bongs"],)
    my_dictionary["bong types"].remove("tall") ### removes a value from the key

    print("\n the value tall was removed:", my_dictionary["bong types"])
    my_dictionary.pop("bong types")           ### delete a value from the dictionarand can display at the same timey\
    print("\nA value from the dictionary was removed", my_dictionary)
    print(my_dictionary.pop("keywords"))
    print(my_dictionary)

##dictionarycommands()

def automatedbrowser():
    import tkinter as tk
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.keys import Keys 
    from selenium.webdriver.common.by import By
    import requests, bs4
    from datetime import date
    import json
    import tkinter as tk
    from tkinter import simpledialog
    from pynput.keyboard import Key, Listener
    ##from tkinter import *

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    a = "IN"
    url = "https://www.visahq.com/algeria/"
    b = "IN"
    driver.get(url)
    time.sleep(1)
    driver.add_cookie({'name' : 'citizenship_alpha2', 'value' : a}) 
    driver.add_cookie({'name' : 'living_in_alpha2', 'value' : b})
    driver.get(url)
    time.sleep(1)
    ##t = driver.find_element(By.ID , "algeria-visa")
    time.sleep(1)
    try:
        text = driver.find_element(By.CLASS_NAME, "visa-info__redirect_url_text").text
        print(text)
        print(f"https://www.{text}/")
        text = f"https://www.{text}/"
        countrycode = url[22:]
        newparsedurl = f"{text}{countrycode}?residency={b}&citizenship={b}"
        
        time.sleep(1)
        text = str(text)
        #input("")
        driver.get(newparsedurl)

        print(a)
        print(b)
    except:
        pass

    #input("")
    automatedbrowser()

##automatedbrowser()
def picklerr():
    import requests, bs4
    import webbrowser
    import re
    import pickle
    import pandas as pd
    import requests, bs4
    import openpyxl
    from datetime import date 

    class User:
        instances = []
        def __init__(self,firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname
    def printt():
        print("cool")
     

    def save(pickle_object): ### this one overwrites
        class User:
            def __init__(self,firstname, lastname):
                self.firstname = firstname
                self.lastname = lastname
       # my_pickled_object =  pickle.dumps(pickle_object)
        with open('learn_pickle','wb') as file:
       #     pickle_object = pickle.dump(my_pickled_object, file)
             pickle.dump(pickle_object, file)

    def load():  #does not load as an array
        infile = open('learn_pickle','rb')
        pickle_transfer = pickle.load(infile)
        pickle_object = pickle.loads(pickle_transfer)
        return pickle_object

    storeclass = []
    User1 = User("malcolm","vernon")
   # User1 = pickle.dumps(User)
    storeclass.append(User1)
    with open('learn_pickle','wb') as file:
        pickle.dump(User1, file)
    print(User1.firstname)
    User2 = User("steven", "schuler")
    storeclass.append(User2)
    print(User1)
    print(User2)
    print(User1)
    ##save(storeclass)
    #save(User1)
    #people = load()
    x = 0
   # print("my people" , people)
    
##objects defined in a function are local objects

#picklerr()
from collections import UserDict
import pickle

class User:
    instances = []
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
storage = []
User1 = User("malcolm","vernon")
storage.append(User1)
print(User1)
User2 = User("Aron", "davis")
print("printing class", User)
storage.append(User2)
with open ('learn_pickle', 'wb') as file:
    pickle.dump(storage,file)
"""""
with open('learn_pickle','wb') as file:
    pickle.dump(User1, file)
    pickle.dump(User2, file)
"""""
infile = open('learn_pickle','rb')
pickle_transfer = pickle.load(infile)
#me = pickle.load(infile)
#print(pickle_transfer.firstname)
#print(me.firstname)
print(pickle_transfer[0].firstname)
counter = 0
for x in pickle_transfer:             ### reads all first names from the class
    print(pickle_transfer[counter].firstname)
    counter += 1




input("")
"""""
https://realpython.com/beautiful-soup-web-scraper-python/
https://www.worthwebscraping.com/how-to-use-cookies-and-session-in-python-web-scraping/
https://realpython.com/python-gui-tkinter/
"""""