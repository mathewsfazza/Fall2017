#MWritten by Mathews Fazza and Jake Swindle for Data and Applications Security CS 4389 - Fall2017
#Assignment 4

import string
import collections
import operator

#decipher shifts the characters down the alphabet
def decipher(i):
    plaintext = ''
    for x in range (cyphertext.__len__()):
        plaintext += alphabet[alphabet.index(cyphertext[x]) - i]    #builds string
    print plaintext                                                 #prints string

#makeTable creates a dictionary in the form {'value of i' : 'value of phi'}
def makeTable():
    for i in range (alphabet.__len__()):
        temp = 0
        for key in fc.keys():                                       #iterate through every key
            temp += (fc[key] * pc[alphabet[alphabet.index(key) - i]])#applies the function to figure out phi
        phiCalc[i] = temp                                           #pairs 'phi' with 'i' in the dictionary



#this is the main section of the program
alphabet = string.ascii_uppercase                       #creates list with all uppercase characters
alphabet[26 % len(alphabet)]                            #wraps list so index -1 will become 25
cyphertext = 'TEBKFKQEBZLROPBLCERJXKBSBKQP'
freq = [0.080, 0.015, 0.030, 0.040, 0.130,              #freq is an array representing the frequency each character
        0.020, 0.015, 0.060, 0.065, 0.005,              #appears in English
        0.005, 0.035, 0.030, 0.070, 0.080,
        0.020, 0.002, 0.065, 0.060, 0.090,
        0.030, 0.010, 0.015, 0.005, 0.020,
        0.002]
pc = dict(zip(alphabet, freq))                          #creates a dictionary in the form {'character' : 'frequency'}
phiCalc = {}                                            #creates a dictionary for the table that has phi values

#question 1A
print "Using brute force, we try every possible solution until we find the plaintext"
for j in range(alphabet.__len__()):
    decipher(j)


#question 1B
print "\n\n\n\n\nNow we try to decipher the text using the method provided in the homework"

fc = collections.Counter(cyphertext)                    #counts the number of times each character appears in cyphertext

for key in fc.keys():                                   #transforms the count into percentages
    fc[key] = float(fc[key])
    fc[key] = float(fc[key] / cyphertext.__len__())


makeTable()                                             #creates list in the form of ordered pairs ['i', 'phi']
phiCalc = sorted(phiCalc.items(), key = lambda x: (-x[1], x[0]))    #sorts list in descending order
phiCalc = map(operator.itemgetter(0), phiCalc)          #reasigns list into array with values of i

for i in range (phiCalc.__len__()):                                 #calls decipher to shift down the characters using 'i's
    decipher(phiCalc[i])                                #with the most 'phi'
