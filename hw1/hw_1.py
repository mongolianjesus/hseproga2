
# coding: utf-8

# In[ ]:


import random
#я не очень большую часть этого кода писала сама, тут в основном просто все собрано со stackoverflow, вроде так можно
def setup():
    print("Welcome to Hangman!")
    print("There are 3 sets of words shown below:")
    print("\t1. dinos")
    print("\t2. pontificate")
    print("\t3. the posthuman")


#выбор темы
def theme_choice():
    user_setting = input("Please choose a set of words by typing its number: ")
    
    if (str(user_setting) == "1"):
        with open('dinos.txt', encoding='utf-8') as f:
            word_list = f.read().splitlines()
        print("\nYou have chosen dinos and will receive 7 lives.")  
        
    elif (str(user_setting) == "2"):
        with open('pontificate.txt', encoding='utf-8') as f:
            word_list = f.read().splitlines()
        print("\nYou have chosen pontificate and will receive 7 lives.") 
        
    elif (str(user_setting) == "3"):
        with open('theposthuman.txt', encoding='utf-8') as f:
            word_list = f.read().splitlines()
        print("\nYou have chosen theposthuman and will receive 7 lives.") 
        
#выбор рандомного слова
    random_num = random.randint(0, len(word_list)-1)
    guessWord = word_list[random_num]
    return guessWord
        
        
        

def playing(theme_choice):
    again = True 
    while again: #loop
        repetitions = []
        guessWord = theme_choice()
        board = "-" * len(guessWord) #нижние подчеркивания вместо букв
        alreadySaid = set()
        mistakes = 7 

        print(" ".join(board))

        guessed = False
        while not guessed and mistakes > 0:
            guess = input('Guess a letter using latin alphabet: ').lower()
            while (guess.isalpha() == False) or len(guess) != 1: #проверка инпута
                    print("Something is wrong with your input.Use latin letters only, 1 symbol per guess.")
                    guess = input('Guess a letter using latin alphabet: ').lower() 
            if guess.isalpha() and len(guess) == 1:
                    if guess in repetitions:
                        print('You have alredy entered this letter. Try some other, there are lots of them.')
                    elif guess in guessWord: 
                        alreadySaid.add(guess)
                        board = "".join([char if char in alreadySaid else "-" for char in guessWord]) #заменяет подчеркивания
                        if board == guessWord: #слово угадано
                                guessed = True
                    else:
                        mistakes -= 1
                        print("Nope.", mistakes, "mistakes left.") 
                    print(" ".join(board))   
            repetitions.append(guess)
                        
                
        print("good job")
        #спрашивает, хочешь ли поиграть еще
        again = (input("Would you like to go again? Print [yes/no]: ").lower() == 'yes') 
setup()
playing(theme_choice)




