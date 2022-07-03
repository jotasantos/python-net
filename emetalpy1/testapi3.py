#!/usr/bin/python3

import packet
import json
import os, time

PROJECT_ID = "19a1ce77-719c-4bd4-929b-430f41552ece"
TOKEN_EMETAL = os.getenv('TOKEN_EMETAL')

def compare_datef(file):
    filedate = os.path.getmtime(file)
    current = time.time()
    interval = current - filedate
    return interval

def watchdog():
    res = packet.Manager(auth_token=(os.getenv('TOKEN_EMETAL')))
    
    # if there's no file and res is not empty, write it down
    if (not os.path.exists('./machines_ids') and res):
        restr = str(res)
        with open ('./machines_ids', 'w') as outfile:
            outfile.write(restr)
            
    elif (not res):
        if os.path.exists('./machines_ids'):
            os.remove('./machines_ids')
    
    else:
        # If yes res + file exists
        if compare_datef('./machines_ids') > 60:
            print('DELETING SERVER!!!!')
            # delete the file only after confirmation from api servers are gone

if __name__ == '__main__':
    watchdog()