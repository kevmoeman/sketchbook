
# coding: utf-8

# In[1]:

def shrinkerv6(string):
    l = []
    i = 1
    count = 1
    l+=string[0]
    while i < len(string):
        if string[i] == string[i-1]:
            count+=1
            i+=1
        elif string[i] != string[i-1]:
            l.append(count)
            l+=string[i]
            count=1
            i+=1
        if i == len(string):
            l.append(count)
    return l

print(shrinkerv6('aaaabbbbbcccccc'))


# In[ ]:

# 2 arrays output 3rd array with the numbers in common
#use dictionary 
#find 2 more ways to do this
def vztest(n, m):
    d = {}
    f = []
    for key in n:
        d[key] = 1
    for i in m:
        if i in d:
            f.append(i)
    return f
print(vztest(['vz', 'rob', "fagit"], ["codder", "dungo", 'vz']))


# In[ ]:




# In[1]:

#Implement an algorithm to determine if a string has all unique characters.
def dupiesmasher(string):
    l = []
    dupes = True
    for n in string:
        if n in l:
            dupes = False
        if n not in l:
            l+=n
            
    return dupes
    
print(dupiesmasher('auo'))

def is_dupes(l):
    if len(l) == len(set(l)):
        return True
    else:
        return False
print(is_dupes('abcdgg'))

        


# In[9]:

#return a list of characters that is only unique letters in a string backwards
def bwardds(string):
    l = []
    for n in set(string):
        if n not in l:
            l+=n
    bwards = l[::-1]
    return bwards

def bwardds2(string):
    l = []
    s = set()

    for n in string[::-1]:
        if n not in s:
            l+=n
            s.add(n)
    return l
print(bwardds2("aabdceaaabbbbcd"))


# In[67]:

#check to see if a two words are 0 or 1 edits away from being identical
def editcheckv3(s1,s2):

    l = ""
    if len(s1) == len(s2):
        for i in range(len(s1)):
            #builds word around changed letter
            l=(s1[:i]+s2[i]+s1[i+1:])
#             print(l)
            if s1 == l:
                return True
                


        
    if len(s1) > len(s2):
        for i in range(len(s1)):
            l=(s1[:i]+s1[i+1:])
            # try removing each character of s1, and seeing if that string matches s2
#             print(l)
            if s2 == l:
                return True
                


    if len(s2) > len(s1):
        for i in range(len(s2)):
            l=(s2[:i]+s2[i+1:])
#             print(l)
            if s1 == l:
                return True
              

    return False


            
        
print(editcheckv3('abca','abc'))


# In[33]:

#word swirlys

#start with true and show false when it doesnt work
def swirlout(word):
    #swirly word if each letter alternates being the farthest letter away
    swirly = True
    direction = 1
    L = word[0]
    R = word[0]
    for i in range(1, len(word)):
        direction = i%2
        cur = word[i]
        if direction == 1:
            if cur < R:
                swirly = False
            R = cur

        if direction == 0:
            if cur > L:
                swirly = False
            L = cur

    return swirly
        # only goes clockwise
def swirlout_counterwise(word):
    #swirly word if each letter alternates being the farthest letter away
    swirly = True
    direction = 1
    L = word[0]
    R = word[0]
    for i in range(1, len(word)):
        direction = (i+1)%2
        #starts with going the other way hahalamo
        cur = word[i]
        if direction == 1:
            if cur < R:
                swirly = False
            R = cur

        if direction == 0:
            if cur > L:
                swirly = False
            L = cur

    return swirly
def swirlin_clockwise(word):
    swirly = True
    direction = 1
    L = word[0]
    R = word[1]
    #initial check to see if the word is clockwise
    if R < L:
        swirly = False
        return swirly
    for i in range(2, len(word)):
        #when i is even update L
        #when i is odd update R
        direction=i%2
        cur = word[i]
        if cur < L or R < cur:
            swirly = False
        if direction == 0:
            L = cur
        if direction == 1:
            R = cur
    return swirly

def swirlin_counterwise(word):
    swirly = True
    direction = 1
    L = word[1]
    R = word[0]
    #initial check to see if the word is counterclockwise
    if R < L:
        swirly = False
        return swirly
    for i in range(2, len(word)):
        #when i is even update R
        #when i is odd update L
        direction=i%2
        cur = word[i]
        if cur < L or R < cur:
            swirly = False
        if direction == 0:
            R = cur
        if direction == 1:
            L = cur
    return swirly


def is_swirl(word):
    if swirlin_clockwise(word):
        print("swirls in clockwise")
    if swirlout(word):
        print('swirls out clockwise')
    if swirlin_counterwise(word):
        print('swirls in counterclockwise')
    if swirlout_counterwise(word):
        print('swirls out counterclockwise')
is_swirl('miner')

        


# In[2]:




# In[3]:




# In[ ]:



