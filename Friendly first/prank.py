import pyfiglet 
import os

user = os.system('whoami')
result = pyfiglet.figlet_format(user, "you have been hacked") 
print(result) 