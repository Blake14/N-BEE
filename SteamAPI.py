import json
import requests
import datetime
from flask import Flask, request
from twilio.twiml.message_response i

app = Flask(_name_)

@app.route('/', methods=['POST'])
def webhook():
  


Steam_User_Id = '76561198068930308'
API_Key = 'AEC32B1127E46161026A08A306280538'

Player_Summary_Url = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_Key}&steamids={Steam_User_Id}'

resp = requests.get(Player_Summary_Url)
resp_json = resp.json()
Steam_Attributes = resp_json["response"]["players"][0]

Steam_Id = Steam_Attributes["steamid"]
Persona_Name = Steam_Attributes["personaname"]
Real_Name = Steam_Attributes["realname"]
Steam_Bday = int(Steam_Attributes["timecreated"])

def Get_Name():
  #print(str(Real_Name))
  return Real_Name
#print(datetime.utcfromtimestamp(Steam_Bday).strftime('%Y-%m-%d %H:%M:%S'))
