import pickle
import random
import sys

a = open('lexicon-luke','rb')
successorlist = pickle.load(a)
a.close()


def nextword(a):
    if a in successorlist:
        try:
            return random.choice(successorlist[a])
        except:
            return ''
    else:
        return 'el'

speech = ''
while speech != 'quit':
    speech = raw_input('>')
    s = random.choice(speech.split())
    response = ''
    while True:
        neword = nextword(s)
        response += ' ' + neword
        s = neword
        if len(response) > 100:
            break
    print response
