def Question1():
    print("""Question 1: What is the capital of France?
a) paris
b) london
c) rome """)
    Question= 'Q1'
    answer1= input("Your answer: ").lower()
    return Question,answer1
def Question2():
    print("""Question 2: What is the largest planet in our solar system?
a) earth
b) jupiter
c) mars """)
    Question= 'Q2'
    answer2= input("Your answer: ")
    return Question, answer2
def check_answer(Question, answer):
    answers={'Q1':'a', 'Q2': 'b'}
    if answers[Question]== answer:
        print("Correct!")
    else:
        print(f"The correct answer is {answers[Question]}")

def main():
    Question, answer1 = Question1()
    check_answer(Question, answer1)
    Question, answer2 = Question2()
    check_answer(Question, answer2)


if __name__ == "__main__":
  main()
