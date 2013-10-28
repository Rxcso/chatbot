#!/usr/bin/env python
# -*- coding: UTF8 -*-
import codecs;
import os;
import datetime;
import re;
import bitly;
import subprocess;
import time;
import sys;
from random import choice;
import lukebot

debug = 0;

saved_tuits_file = "/data/projects/aniversario_peru/saved_tuits.txt"
mentions_file = "/data/projects/aniversario_peru/mentions.csv"

# t update "mi primer tuit"
cmd2 = '/usr/local/bin/t set active AniversarioPeru'
p = subprocess.check_call(cmd2, shell=True);

def get_mentions():
    if debug:
        cmd = "cat debug_tuits.txt | grep -i " + user + " | head -n 1"
        p = subprocess.check_output(cmd, shell=True);
    else:
        cmd = "/usr/local/bin/t mentions -l -c"
        p = subprocess.check_output(cmd, shell=True);
        f = open(mentions_file, "w")
        f.write(p)
        f.close()

def get_last_tuit(user):
    if debug:
        cmd = "cat debug_tuits.txt | grep -i " + user + " | head -n 1"
        p = subprocess.check_output(cmd, shell=True);
    else:
        cmd = "cat " + mentions_file + " | grep -i " + user + " | awk -F ',' '{if($3 == \"" + user + "\") print $0}' | head -n 1"
        p = subprocess.check_output(cmd, shell=True);
    if len(p) > 0:
        p_ = p.split(",")
        tuit_id = p_[0]
        tuit_date = p_[1]
        message = p_[3]
        message = message.replace('"', '')
        message = re.sub("\s*@AniversarioPeru\s*", "", message, re.I)
        return {
                "tuit_id": tuit_id, 
                "tuit_date": tuit_date, 
                "user": user, 
                "message": message
                }
    return "none"

def is_new_tuit(tuit):
    # file full of tuits
    f = open(saved_tuits_file, "r")
    file = f.readlines();
    f.close()
    is_new_tuit = "true"
    for line in file:
        line = line.strip()
        line = line.split(",")
        print line
        if line[0] == tuit['tuit_id'] and line[2] == tuit['user']:
            is_new_tuit = "false"

    return is_new_tuit

def get_message(frases_to_reply):
    return choice(frases_to_reply)
    

def reply(tuit):
    #message = get_message(frases_to_reply)
    message = lukebot.get_response(tuit['message'])
    cmd = "/usr/local/bin/t reply " + tuit['tuit_id'] + " '" + message + "'"
    p = subprocess.check_call(cmd, shell=True);

users = [
        "addTrollUser"
        ]

get_mentions()
for user in users:
    tuit = get_last_tuit(user)
    if tuit != "none":
        # is the last tuit a new one?
        if is_new_tuit(tuit) == "true":
            reply(tuit)
            # save tuit
            f = open(saved_tuits_file, "a")
            f.write(tuit['tuit_id'] + "," + tuit['tuit_date'] + "," + tuit['user'] + "\n")
            f.close()
        else:
            print "we replied already"

