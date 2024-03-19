"""
   init content 
   
"""

db = "../db/users.db"
import json
import hashlib
import random

uname =input("username %")
passwd = input("password %")
handle = input("handle %")
modle_number = int(random.randint(1000,10000))

for index in range(modle_number):
    if index == modle_number:
        continue
modle = index
def encrypt(wd):
    format = hashlib.md5()
    format.update(wd.encode('utf-8'))
    return format.hexdigest()
class User:
    def __init__(self,username,password,handle,model_number):
        self.username = username
        self.model_number = model_number
        self.handle = handle
        self.password = password
    
    def setUser(self, username, password,handle):
        username = self.username
        password = self.password
        handle = self.handle
    
    def login(self):
        pass
    
    def getUser(self, username,passwd,modle):
        with open(db,'r') as query:
            output = query.read()
            print(set(output))
    
    def logout(self):
        pass
    
    def create(self):
        # self.username,self.model_number,self.handle
        tag = {
            handle:{
                "username": uname,
                "password": encrypt(passwd),
                "model_number": modle
            }
               }
        with open(db,'+a') as manager:
            # manager.write(f"{json.dumps(tag)}\n")
            json.dumps(manager.write(f"{tag},\n"))
        


newUser = User(username=uname,password=passwd,handle=handle,model_number=modle_number)

newUser.getUser(username=uname,passwd=passwd,modle=modle)
