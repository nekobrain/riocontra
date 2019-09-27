import string
from syllabipy.sonoripy import SonoriPy

words_not_to_riocontrarize = ['come', 'dove', 'quando', 'perché', 'perchè', 'proprio', 'davvero', 'tanto', 'troppo', 'questo', 'questa', 'quello', 'quella']

def checkDoubleConsonant(s):
    if s[0] == s[-1] and s[0] not in ['a', 'e', 'i', 'o', 'u']:
        return s[-1] + s[:-1]
    else:
        return s

def riocontrarizeLongWords(arr):
    riocontra_index = len(arr) - 2
    return checkDoubleConsonant(''.join(arr[:riocontra_index]) + ''.join(arr[riocontra_index:][::-1]))

def riocontra(s): 
    endings = ['.', '?', '!']
    ending = ''
    if s[len(s)-1] in endings:
        ending = s[len(s)-1]
        s = s[:-1]
    if ' ' in s:
        ret = ''
        s = s.split(' ')
        for w in s:
            if w.lower() in words_not_to_riocontrarize:
                ret += w + ' '
                continue
            elif w.lower() == 'zio':
                ret += 'ozi' + ' '
                continue
            elif w.lower() == 'troia':
                ret += 'iatro' + ' '
                continue
            input = SonoriPy(w)
            if len(input) == 1:
                ret += input[0] + ' '
            elif len(input) > 3:
                ret += riocontrarizeLongWords(input) + ' '
            else:
                ret += checkDoubleConsonant(input[-1] + ''.join(input[:-1])) + ' '
        return ret.rstrip() + ending
    input = SonoriPy(s) 
    if len(input) > 3:
        return riocontrarizeLongWords(input) + ending
    else:
        return checkDoubleConsonant(input[-1] + ''.join(input[:-1])) + ending
