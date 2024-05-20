import subprocess
import time

user = subprocess.getoutput('whoami').strip()

result = "Hacker : " + user + " you have been hacked \n" + "you have three chances to call me what you shall call me"
print(result)
i = 3
while(i>0):
    print(i)
    inp = input("{} : ".format(user))
    if(inp != "dad"):
        i = i-1
    else:
        print("you shall be spared for now")
        break

time.sleep(1)
if(i<=0):
    if inp!= "dad":
        print("....")
        time.sleep(5)
        print("you are fucked")
        time.sleep(1)