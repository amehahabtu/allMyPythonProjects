# words that matched with initialized word.
def word_matched():    
    user_word=' '
    while (user_word != 'chupacabra'):
        user_word=input("Enter the word: ")
        if user_word=='chupacabra':
            break
    print("You have successfully left the loop !")
# word_matched()

# printout words without vowels
def Get_letters_fromuserword_without_vowels():    
    vowel='AEIOU'
    user_word=input("Enter the word: ").upper()
    for letter in user_word :
        #print(letter)
        if letter in vowel:
            continue
        print(letter)
#Get_letters_fromuserword_without_vowels()

#  Get words without vowel from user word entered
def Get_combinedleters_withnovowels():    
    vowels='AEIOU'
    words_without_vowels=' '
    user_word=input("Enter the word: ").upper()
    for letter in user_word:
        if letter not in vowels:
            words_without_vowels += letter
    print("Words without volwels are:",words_without_vowels)
# Get_combinedleters_withnovowels()
