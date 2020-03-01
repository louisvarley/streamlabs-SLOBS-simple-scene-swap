#!/usr/bin/python
# -*- coding: utf-8 -*-

#---------------------------------------
# Import Libraries
#---------------------------------------
import clr
clr.AddReference("IronPython.Modules.dll")
import os
import json
import re
import time
import threading

#---------------------------------------
# Script Information
#---------------------------------------
ScriptName = "Scene Swap"
Website = "http://www.github.com/Bare7a/Streamlabs-Chatbot-Scripts"
Description = "Hit 2 Keys with a Time Between"
Creator = "Louis Varley"
Version = "1.3.0"

#---------------------------------------
# Global Vars
#---------------------------------------
BridgeApp = os.path.join(os.path.dirname(__file__), "bridge\\SLOBSRC.exe")
RegObsScene = None
RegObsSource = None
RegObsSourceT = None
RegObsFolder = None
RegObsFolderT = None
RegObsSwap = None
RegObsReplaySwap = None

#---------------------------------------
# Settings Vars
#---------------------------------------
configFile = "config.json"
settings = {}
usersFile = "users.txt"
userList = []
blackList = {}
delay = 5

#---------------------------------------
# Functions SRCP
#---------------------------------------

def Logger(response):
        """ Logs response from bridge app in scripts logger. """
        if response:
                Parent.Log(ScriptName, response)
        return

def ChangeScene(scene, delay=None):
        """ Change to scene. """
        if delay:
                Logger(os.popen("{0} change_scene \"{1}\" {2}".format(BridgeApp, scene, delay)).read())
        else:
                Logger(os.popen("{0} change_scene \"{1}\"".format(BridgeApp, scene)).read())
        return

def ChangeSceneTimed(scene, delay, returnscene=None):
        """ Swap to scene and then back or to optional given scene. """
        if returnscene:
                Logger(os.popen("{0} swap_scenes \"{1}\" {2} \"{3}\"".format(BridgeApp, scene, delay, returnscene)).read())
        else:
                Logger(os.popen("{0} swap_scenes \"{1}\" {2}".format(BridgeApp, scene, delay)).read())
        return

def ThreadedFunction(command):
        Logger(os.popen("{0} {1}".format(BridgeApp, command)).read())
        return
        
#---------------------------------------
# Functions Script
#---------------------------------------        
        
def OpenReadMe():
        """ Open the script readme file in users default .txt application. """
        os.startfile("https://ocgineer.com/sl/chatbot/slobsremote.html")
        return  

def ScriptToggled(state):
    return

def Init():
    global settings, usersFile, userList

    path = os.path.dirname(__file__)
    usersFile = os.path.join(path, usersFile)

    try:
        with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
            settings = json.load(file, encoding='utf-8-sig')
    except:
        settings = {
            "offlineOnly": True,
            "command": "!swap",
            "scene1": "",
            "scene2": "",
            "sceneDelay": 5,
            "sceneChangeMessage": "$user, wants to change the scene!",      
            "sceneReturnMessage": "",                               
            "permission": "Everyone",                 
            "useCooldown": True,
            "useCooldownMessages": True,
            "cooldown": 1,
            "onCooldown": "$user, $command is still on cooldown for $cd minutes!",
            "userCooldown": 300,
        }
                                    
    return

def Execute(data):
    global userList, blackList
    
    if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and (settings["offlineOnly"] and (not Parent.IsLive()) or (not settings["offlineOnly"])):
        
                userId = data.User
                username = data.UserName

                Parent.SendStreamMessage("changing scene") 
                                
                Parent.SendStreamMessage("changing scene") 
                                
                ChangeSceneTimed("Intro", 5, "Streaming Multi")
                                
                Parent.SendStreamMessage("and back") 

                time.sleep(3000)
      
    return

def ReloadSettings(jsonData):
    Init()
    return

def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.txt")
    os.startfile(location)
    return

def Tick():
    global resetTime, delayTime, delay, userList, blackList, settings

    return
