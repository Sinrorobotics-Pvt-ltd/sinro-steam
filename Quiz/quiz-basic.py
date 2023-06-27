import sys

# List for storing questions
QueList = [
    "Who developed C?",
    "Who developed Python?",
    "When was Python released?",
    "Which of the following is not a keyword?",
    "What is the answer to this expression, 22 % 3 is?"
]

# List for storing options
OptList = [
    ["Denish Ritchie", "Bjarne Stroustrup", "James Gosling", "Tim Berners Lee"],
    ["Denish Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"],
    ["1992", "1991", "1990", "1994"],
    ["assert", "nonlocal", "pass", "eval"],
    ["5", "7", "1", "0"]
]

# List for storing correct outputs
OutList = ["1", "4", "2", "4", "3"]

# Initialize variables i and result with 0
i = result = 0

# Function to display the result
def display_result():
    total_questions = len(QueList)
    correct_answers = result
    incorrect_answers = total_questions - result
    percentage = (correct_answers / total_questions) * 100
    
    print("Result:")
    print("Total Questions:", total_questions)
    print("Correct Answers:", correct_answers)
    print("Incorrect Answers:", incorrect_answers)
    print("Percentage:", percentage, "%")

# Function to process the user's input
def process_input(choice):
    global i, result
    
    if choice == OutList[i-1]:
        result += 1

    if i != len(QueList):
        i += 1
        display_question()
    else:
        display_result()
        sys.exit()

# Function to display the current question
def display_question():
    print("Q.", i, QueList[i-1])
    options = OptList[i-1]
    
    for j, option in enumerate(options, start=1):
        print(j, option)

    choice = input("Select an option (1-4): ")
    process_input(choice)

# Main program
print("Python Quiz Application")
print("-----------------------")

while True:
    display_question()
