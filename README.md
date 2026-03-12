# Formative Demo – Python Quiz

For the **Intensive Foundations of Computer Science and Programming** course at [Northeastern University London](https://www.nulondon.ac.uk/).

This demo shows how a simple Python program can run in the terminal without installing Python locally.

The program asks the user a maths question and checks the answer.

## User Instructions

### Installing Python

- Download Python from [the official website](https://www.python.org/downloads)

- Follow the installation instructions for your operating system.

### Running the program

Navigate to the folder containing the file and run:

```bash
python main.py
```

### Playing the quiz

2. A question will appear in the terminal.
3. Type your answer and press Enter.
4. The program will tell you whether your answer is correct.

#### Example gameplay:

```text
Welcome to our quiz
What is 3 * 7?
21
That is correct!!!
```

## Technical Documentation

The code example is below.

```python
import random


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("That is correct!!!")
    else:
        print("That is incorrect!!!")


print("Welcome to our quiz")

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

correct_answer = num_1 * num_2

terminal_answer = int(input(f"What is {num_1} * {num_2}? "))

check_answer(terminal_answer, correct_answer)

