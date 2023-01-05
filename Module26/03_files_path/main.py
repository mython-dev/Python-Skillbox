# TODO здесь писать код

 import os

 import getpass

 user  = getpass.getuser()


 for address, dirs, files in os.walk('/Users/'+user): 
     for name in files:
         print(os.path.join(address))