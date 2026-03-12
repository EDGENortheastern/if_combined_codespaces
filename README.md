# Python Quiz

A demo on how to do the assessments without local Python.

## Technical Documentation

My code example is below

```python
import random
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("That is correct!!!")
    else:
        print("That is Incorrect!!!")

print("Welcome to our quiz")

num_1 = random.randint(1,10)
num_2 = random.randint(1,10)
correct_answer = num_1*num_2

terminal_answer = int(input(f"What is {num_1} * {num_2}"))

check_answer(terminal_answer, correct_answer)
```

