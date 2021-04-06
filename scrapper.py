import random
import time
import string
import requests
import json
from json import loads
from requests import Session
from colorama import Fore, init
init(autoreset=True)

text = """
╋╋╋╋┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┓
┏┳┳━┫┗┳┓┏━┳┳┓┏━┳┳┳━┳┳┳━┓┃━╋━┳┳┳━┓┏━┳━┳━┳┳┓
┃┏┫╋┃╋┃┗┫╋┣┃┫┃╋┃┏┫╋┃┃┃╋┃┣━┃━┫┏┫╋┗┫╋┃╋┃┻┫┏┛
┗┛┗━┻━┻━┻━┻┻┛┣┓┣┛┗━┻━┫┏┛┗━┻━┻┛┗━━┫┏┫┏┻━┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋┗━┛╋╋╋╋╋┗┛╋╋╋╋╋╋╋╋╋╋┗┛┗┛
by boboMbobo | https://github.com/bobombobo/
"""

print(text)
run_ammount = input("input times to run: ")
run_ammount_int=int(run_ammount)
runtime=0
goodgroups = {}
groupsfound=0
groupswithbuildersclub=0

while run_ammount_int>runtime:
  runtime=runtime+1
  id = ''.join(random.choice(string.digits) for i in range(7))
  group = requests.get('https://groups.roblox.com/v1/groups/' + id)
  if group.status_code == 200:
    print("-------------------------------------")
    #print(group)
    #print(id)
    groupsfound=groupsfound+1
    print("id: " + str(id))
    print("Group name: " + group.json()["name"])
    if group.json()["memberCount"] == 0:
      print(Fore.RED + "Member count: " + str(group.json()["memberCount"]))
    else:
      print("Member count: " + str(group.json()["memberCount"]))
    
    if group.json()['publicEntryAllowed'] == True:
      print(Fore.CYAN + "Allowed entry: " + str(group.json()['publicEntryAllowed']))
    else:
      print("Allowed entry: " + str(group.json()['publicEntryAllowed']))

    #finally just doing this lol
    info=group.json()
    #data = json.loads(info)
    if group.json()['owner'] == None:
      print("No owner?")
      print(group.json()['owner'])
    else:
      print("Owner username: " + info['owner']['username'])
      if info['owner']['buildersClubMembershipType'] == ('None'):
        print("DAMN THEY BROKE")
        print(Fore.RED + "Bilders club membership: " + info['owner']['buildersClubMembershipType'])
      else: 
        print(Fore.MAGENTA + "Bilders club membership: " + info['owner']['buildersClubMembershipType'])
        groupswithbuildersclub=groupswithbuildersclub+1

    #print("Owner: " + str(group.json()['owner']))
    if group.json()['owner'] == None and group.json()['publicEntryAllowed'] == True:
        print(Fore.GREEN + "https://www.roblox.com/groups/" + str(id))
        print("Avalible json data:\n " + str(group.json()))
        wait(10)
        goodgroups.append("https://www.roblox.com/groups/" + str(id))
        print("-------------------------------------")

    else:
      pass

  elif group.status_code == 400:
      pass

  else:
      pass

print("")     
print(goodgroups)
print("")

print("Some fun math stuff:")
print("Groups found: " + str(groupsfound) + "/" + run_ammount)
groupmath=(100*(1-(groupsfound/run_ammount_int)))
print("Ammount lost (%): %" + str(groupmath))


print("groups with builders club sub: " + str(groupswithbuildersclub) + "/" + run_ammount)
try: 
  buildersmath=(100*(1-(run_ammount_int/groupswithbuildersclub)))
  print("Groups with builders club (%): %" + str(buildersmath))
except:
  print("Groups with builders club (%): %0.0")
