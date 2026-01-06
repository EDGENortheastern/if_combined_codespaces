def my_function(user_answer):
    if user_answer == 4:
        print("That is correct!!!")
    else:
        print("That is INcorrect!!!")

print("Welcome to out quiz")

terminal_answer = int(input("What is 2 plus 2"))

my_function(terminal_answer)