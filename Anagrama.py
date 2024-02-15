def main():
    word1 = "amor"
    word2 = "roma"
    word1low = word1.lower()
    word2low =word2.lower()
    char_word1 = list(word1low)
    char_word2 = list(word2low)
    char_word1ordenado = char_word1.sort()
    char_word2ordenado = char_word2.sort()
    # si son la misma palabra: falso
    if word1low == word2low:
        print ("false")
    # si es un anagrama, verdadero
    elif char_word1ordenado ==  char_word2ordenado:
        print ("true")
    #en cualquier otro caso, falso
    else:
        print ("false")
        
main()
        
        
