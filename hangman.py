from nltk.stem import WordNetLemmatizer
import random
lemmatizer = WordNetLemmatizer()
f = open("wordlist.txt", "r")
realword = lemmatizer.lemmatize(random.choice(f.read().split()))
realword_list = list(realword)
display_list = list('_' * (len(realword_list)))
chances = 6
while chances:

    check = (input('Enter letter')).lower()
    i = 0
    if check in realword_list:

        for i in range(len(realword_list)):
            if check == realword_list[i]:
                display_list[i] = check
        print(display_list)
        if display_list == realword_list:
            break
    else:
        chances = chances - 1
        print("You have "+str(chances)+" remaining")
if chances > 0:
    print("Correct! You win")
else:
    print("Oops..You lose! \nCorrect Word is :" +realword)
