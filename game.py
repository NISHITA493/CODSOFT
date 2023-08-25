import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Test your knowledge on the chosen topic.")
        print("Each question has multiple-choice answers.")
        print("Let's begin!\n")

    def present_quiz_questions(self):
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}: {question['question']}")
            for j, choice in enumerate(question['choices'], start=1):
                print(f"{j}. {choice}")
            user_answer = input("Your answer (number): ")
            self.evaluate_user_answer(question, int(user_answer))

    def evaluate_user_answer(self, question, user_answer):
        correct_answer = question['correct_answer']
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect. The correct answer was:", question['choices'][correct_answer - 1], "\n")

    def display_final_results(self):
        print("Quiz Completed!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}")

        if self.score == len(self.questions):
            print("Congratulations! You got all the questions right.")
        elif self.score >= len(self.questions) / 2:
            print("Good job! You did well.")
        else:
            print("Keep practicing to improve your score.")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ")
        return play_again.lower() == 'yes'


# Define your quiz questions
quiz_questions = [
    {
        'question': "What is the capital of France?",
        'choices': ["Paris", "London", "Berlin"],
        'correct_answer': 1
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'choices': ["Mars", "Jupiter", "Venus"],
        'correct_answer': 1
    },
    # Add more questions here...
]

# Initialize the quiz game
quiz = QuizGame(quiz_questions)
quiz.display_welcome_message()

play = True
while play:
    quiz.present_quiz_questions()
    quiz.display_final_results()
    play = quiz.play_again()
