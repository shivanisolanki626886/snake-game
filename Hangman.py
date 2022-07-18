import random
def hangmen():
    print("hello word")
    list_of_words=['eduyear','hangmen','india','laptop']
    word=random.choice(list_of_words)
    print(word)
    turns=10
    guessmade=""
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word=""
        
        
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print("you won!!!!")
        print("guess the words",main_word)
        guess=input()
        
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
            guess=input()
        
        if guess not in word:
            turns=turns-1
            
            
            if turns==9:
                print("9 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
            if turns==8:
                print("8 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
                print("        o        ")  
            if turns==7:
                print("7 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
                print("        o        ") 
                print("        |        ")
            if turns==6:
                print("6 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
                print("        o        ") 
                print("        |        ")
                print("       /         ")
            if turns==5:
                print("5 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
                print("        o        ") 
                print("        |        ")
                print("       / \       ")
            if turns==4:
                print("4 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
                print("       \o/       ") 
                print("        |         ")
                print("       / \         ")
            if turns==3:
                print("3 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
                print("       \o/        ") 
                print("        |        ")
                print("       / \       ")
            if turns==2:
                print("2 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
                print("       \o/ |     ") 
                print("        |        ")
                print("       / \       ")
            if turns==1:
                print("only 1 turn left!!! hangmen on this last breath") 
                print("_ _ _ _ _ _ _ _ _")
                print("       \o/_|     ") 
                print("        |        ")
                print("       / \       ")    
            if turns==0:
                print("you loose")
                print("you let a good man die")
                print("0 turn left!!!") 
                print("_ _ _ _ _ _ _ _ _")
                print("       \o/_|     ") 
                print("        |        ")
                print("       / \       ")
                break



name=input("ENTER YOUR NAME->")
print("welcome",name,"!")
print("_ _ _ _ _ _ _ _ _")
print("try to guess the word in the less then 10 attempts")
hangmen()