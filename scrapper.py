#Roblox group scraper v2
import random
from time import sleep
import string
import requests
import json
from json import loads
from requests import Session
from colorama import Fore, init
init(autoreset=True)


text1 = (Fore.RED + """
╋╋╋╋┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┓
┏┳┳━┫┗┳┓┏━┳┳┓┏━┳┳┳━┳┳┳━┓┃━╋━┳┳┳━┓┏━┳━┳━┳┳┓
┃┏┫╋┃╋┃┗┫╋┣┃┫┃╋┃┏┫╋┃┃┃╋┃┣━┃━┫┏┫╋┗┫╋┃╋┃┻┫┏┛
┗┛┗━┻━┻━┻━┻┻┛┣┓┣┛┗━┻━┫┏┛┗━┻━┻┛┗━━┫┏┫┏┻━┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋┗━┛╋╋╋╋╋┗┛╋╋╋╋╋╋╋╋╋╋┗┛┗┛
""" + Fore.GREEN + """Roblox group scrapper (v2 recode) | by boboMbobo | https://github.com/bobombobo/
"""+ Fore.WHITE + """ID generation generation types:

[1] Generation via a range of numbers ex: checks all groups with id's between 2,000,000 and 2,010,000
[2] Random 7 digit number (can be changed to different digit lenght)
""")

print(text1)

#choice=int(input("--->>>"))

runtime=0
goodgroups = []
groupsfound=0
groupswithbuildersclub=0
run_ammount_int=0

choice=int(input("[1] Range\n[2] Random\n--->>>"))

def scrape(int_id):
  id=str(int_id)
  group = requests.get('https://groups.roblox.com/v1/groups/' + id)
  if group.status_code == 200:
    print("-------------------------------------")
    #print(group)
    #print(id)
    global groupsfound
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
        sleep(1)
        goodgroups.append("https://www.roblox.com/groups/" + str(id))
        print("-------------------------------------")

    else:
      pass

  elif group.status_code == 400:
      pass
  else:
      pass


if choice==1:
  print("Scraping id range:")
  min_ = int(input("Min: "))
  max_1 = int(input("Max: "))
  max_=int(max_1+1)
  for x in range(min_,max_):
    scrape(x)
  run_ammount_int=max_-min_

if choice==2:
  run_ammount = input("input times to run: ")
  run_ammount_int=int(run_ammount)
  while run_ammount_int>runtime:
    id = ''.join(random.choice(string.digits) for i in range(7)) #Generates random number with 7 digits in the range(x) where x is the digit length
    runtime=runtime+1
    scrape(id)



print("")     
print(goodgroups)
print("")
print("Groups found: " + str(groupsfound) + "/" + str(run_ammount_int))
groupmath=(100*(1-(groupsfound/run_ammount_int)))#I hate math so much dude had think for a bit to whip this up
print("Ammount lost (%): %" + str(groupmath))
