questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["a) Central Processing Unit", "b) Computer Processing Unit", "c) Control Processing Unit", "d) Central Power Unit"],
        "answer": "a"
    },
    {
        "question": "What is the function of RAM in a computer?",
        "options": ["a) Long-term storage of data", "b) Temporary storage of data and programs currently being used", "c) Execution of arithmetic operations", "d) Graphics processing"],
        "answer": "b"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["a) Hyperlinks and Text Markup Language", "b) Hypertext Markup Language", "c) Home Tool Markup Language", "d) High-Tech Markup Language"],
        "answer": "b"
    },
    {
        "question": "Which programming language is often used for web development and is designed to be easy to learn?",
        "options": ["a) Python", "b) C++", "c) Java", "d) JavaScript"],
        "answer": "d"
    },
    {
        "question": "Which data type is used to store whole numbers in Python?",
        "options": ["a) float", "b) int", "c) str", "d) bool"],
        "answer": "b"
    },
]

input("Press enter whenever you are ready to start.\n")
score = 0

for question in questions:
    print(question['question'])
    for option in question['options']:
        print(option)
    answer = input("Enter your choice: ").lower()
    while answer not in "abcd":
        print("Invalid choice. Try again")
        answer = input("Enter your choice: ")
    if answer == question['answer']:
        score += 1

print(f"Your score: {score}/{len(questions)} ({round((score/len(questions)*100), 2)}%)")
