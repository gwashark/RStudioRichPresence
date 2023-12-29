from pywinauto import Desktop
from pyautogui import alert
from discordrp import Presence

import time

windows = Desktop(backend="uia").windows()
roblox_window = [w.window_text() for w in windows if "Roblox Studio" in w.window_text()]
if roblox_window:
    
    try:
        with Presence("1190374257700646982") as drp:
            starttime = int(time.time())
            while True:
                windows = Desktop(backend="uia").windows()
                windowname = [w.window_text() for w in windows if "Roblox Studio" in w.window_text()]
                if not len(windowname) == 0:
                    winstate = windowname[0].split("-")
                    if len(winstate) == 1:
                        drp.set({
                            "state":"Main Menu",
                            "assets":{
                                "large_image": "studio", 
                                "large_text": "Roblox Studio"
                            },
                            "timestamps": {
                                "start": starttime
                            }
                        })
                    elif len(winstate) == 2:
                        drp.set({
                            "state":"Working on game",
                            "details":winstate[0],
                            "assets":{
                                "large_image": "studio", 
                                "large_text": "Roblox Studio"
                            },
                            "timestamps": {
                                "start": starttime
                            }
                        })
                    elif len(winstate) == 3:
                        drp.set({
                            "state":"Scripting in " + winstate[1],
                            "details":winstate[0],
                            "assets":{
                                "large_image": "studio", 
                                "large_text": "Roblox Studio"
                            },
                            "timestamps": {
                                "start": starttime
                            }
                        })
                    time.sleep(3)
                else:
                    drp.clear()
                    exit()
    except Exception as err:
        print(str(err))
        if str(err) == "Cannot find a Windows socket to connect to Discord":
            alert(text='Before Running, please open Discord.', title="Discord Not Detected")
        else:
            alert(text='There was an error while running the presence.\n\n' + str(err) + "\n\n Please report this to the github repository.", title='Presence Error', button='OK')
else:
    alert(text='Before Running, please open Roblox Studio.', title='Roblox Studio Not Detected', button='OK')