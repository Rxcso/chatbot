import pickle
import random
import sys
import re

a = open('lexicon-luke','rb')
successorlist = pickle.load(a)
a.close()

avoid = ["que", "la", "del", "esta", "de", "su", "con"]

def nextword(a):
    if a in successorlist:
        try:
            return random.choice(successorlist[a])
        except:
            return ''
    else:
        return 'de'

speech = ''
while speech != 'quit':
    speech = raw_input('>')
    s = random.choice(speech.split())
    response = ''
    while True:
        neword = nextword(s)
        if neword != '':
            response += ' ' + neword
        s = neword
        if len(response) > 100:
            for i in avoid:
                regex = re.compile('%s\s*$'%i, re.I)
                if regex.search(response):
                    response = regex.sub("", response).strip()
                    
            break
    print response
