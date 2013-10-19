import pickle
import random
import sys
import re

a = open('lexicon-luke','rb')
successorlist = pickle.load(a)
a.close()

avoid = ["en", "el", "que", "la", "del", "esta", "de", "su", "con"]

def nextword(a):
    if a in successorlist:
        try:
            return random.choice(successorlist[a])
        except:
            return ''
    else:
        return 'de'

def get_response(input):
    response = ''
    s = random.choice(input.split())
    while True:
        neword = nextword(s)
        if neword != '':
            response += neword + ' '
        s = neword
        if len(response) > 120:
            for i in avoid:
                regex = re.compile('\s%s\s*$'%i, re.I)
                if regex.search(response):
                    response = regex.sub("", response).strip()
                    
            break
    return response.strip()


if __name__ == "__main__":
    speech = ''
    while speech != 'quit':
        speech = raw_input('>')
        response = get_response(speech)
        print response
