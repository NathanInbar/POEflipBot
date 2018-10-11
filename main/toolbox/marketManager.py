#from toolbox.general import *
#from toolbox.webscraper import *
'''
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('POEflipBot-5ef914e19a0d.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("POE Market Data").sheet1 # open sheet

all_cells = sheet.range('A1:C6')
for cell in all_cells:
    print (cell.value)
'''
