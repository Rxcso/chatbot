import pickle
import sys

# Modified from http://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/

b = open('tradiciones_peruanas.txt')
text = []
for line in b:
    line = line.strip()
    for word in line.split():
        text.append(word)

b.close()

textset = list(set(text))

follow={}
for w in range(len(text)-1):
    check = text[w]
    next_word = text[w+1]
    print check
    print next_word
    if check[-1] not in '(),.?!':
        if follow.has_key(check):
            follow[check].append(next_word)
        else:
            follow[check] = [next_word]

a = open('lexicon-luke','wb')
pickle.dump(follow,a,2)
a.close()
