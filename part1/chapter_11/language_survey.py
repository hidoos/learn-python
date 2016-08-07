from survey import AnonymousSurvey

# define a question. then create object that is about language
question = 'What lauguage did you first learn to speak?'
my_survey = AnonymousSurvey(question)

# show question and store response
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("language: ")
    if response == 'q':
        break
    
    my_survey.store_response(response)

# show survey result
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results() 