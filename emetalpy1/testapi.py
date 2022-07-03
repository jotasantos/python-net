#!/usr/bin/python3

# import packet
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
    res = packet.Manager(auth_token=(os.getenv('TOKEN_EMETAL'))
    
    # if there's no file and res is not empty, write it down
    if (not os.path.exists('./machines_state') and res):
        json_object = json.dumps(res, indent = 2)
        with open ('./machines_state', 'w') as outfile:
            outfile.write(json_object)

    elif not res:
        
        if os.path.exists('./machines_state'):
            os.remove('./machines_state')
    
    if compare_datef('./machines_state') > 60:
        print('DELETING SERVER!!!!')
        # delete the file only after confirmation from api servers are gone

if __name__ == '__main__':
    watchdog()