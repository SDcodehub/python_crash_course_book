from survey import AnonymousSurvey

question = "what language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()

print("Enter 'q' at any time to quite.\n")

while True:
    response = input("language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

print("Thank you for survey")
language_survey.show_results()