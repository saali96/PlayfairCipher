# code referenecd from https://python.algorithmexamples.com/web/ciphers/playfair_cipher.html
import itertools

#using this function to break the string in the tuples of 2
def StringTokenizer(string, StringSize):
    iterate = iter(string)
    while True:
        #using a library itertools to split the characters into a tuple of 2 and return
        tokens = tuple(itertools.islice(iterate, StringSize))
        if not tokens:
            return
        yield tokens
        
#using removeX function to removes the duplicates and replaces them with X
#and remove spaces and a cleaned string is returned at the end
def removeX(originalString):    
    #making the string Upper Case
    originalString = originalString.upper()
    #removing the spaces from the string
    originalString = originalString.replace(' ',"")
    cleanString = ""
 
    if len(originalString) < 2:
        return originalString
 
    for i in range(len(originalString) - 1):
        cleanString += originalString[i]
        #checking for duplicte characters and replacing with X if any
        if originalString[i] == originalString[i + 1]:
            cleanString += "X"
            
    cleanString += originalString[-1]
    
    if(len(cleanString) & 1):
        cleanString += "X"
        
    return cleanString

#creates the table grid with our given key and returns the table grid
def CreateTableGrid(SecretKey):
 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ0123456789"
    grid = []
    #copying SecretKey characters in table grid after checking if they appears to
    #be in the alphabet string
    for char in SecretKey.upper():
        if char not in grid and char in alphabet:
            grid.append(char)
    #filling the remaining table with rest of the alphabets and characters 
    for char in alphabet:
        if char not in grid:
            grid.append(char)
    print(grid)
    return grid
 

    
def encode(plainString, SecretKey):
    tableGrid = CreateTableGrid(SecretKey)
    cleanString = removeX(plainString)
    encodedString = ""
 
    for char1, char2 in StringTokenizer(cleanString,2):
        row1, col1 = divmod(tableGrid.index(char1), 5)
        row2, col2 = divmod(tableGrid.index(char2), 5)
 
        if row1 == row2:
            encodedString += tableGrid[row1 * 5 + (col1 + 1) % 5]
            encodedString += tableGrid[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            encodedString += tableGrid[((row1 + 1) % 5) * 5 + col1]
            encodedString += tableGrid[((row2 + 1) % 5) * 5 + col2]
        else:  # rectangle
            encodedString += tableGrid[row1 * 5 + col2]
            encodedString += tableGrid[row2 * 5 + col1]
    print(encodedString)
    return encodedString


# In[5]:


encode('Input String','secret23')


# In[ ]:




