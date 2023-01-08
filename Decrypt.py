import itertools
#code referenced from https://python.algorithmexamples.com/web/ciphers/playfair_cipher.html
#using this function to break the string in the tuples of 2
def StringTokenizer(string, StringSize):
    iterate = iter(string)
    while True:
        #using a library itertools to split the characters into a tuple of 2 and return
        tokens = tuple(itertools.islice(iterate, StringSize))
        if not tokens:
            return
        yield tokens

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
 

def decode(ciphertext, SecretKey):
    table = CreateTableGrid(SecretKey)
    plaintext = ""
 
    for char1, char2 in StringTokenizer(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
 
        if row1 == row2:
            plaintext += table[row1 * 5 + (col1 - 1) % 5]
            plaintext += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[((row1 - 1) % 5) * 5 + col1]
            plaintext += table[((row2 - 1) % 5) * 5 + col2]
        else:  # rectangle
            plaintext += table[row1 * 5 + col2]
            plaintext += table[row2 * 5 + col1]
    return plaintext


# In[3]:


d=decode('HOMXSESTHOKU','secret23')
print(d)






