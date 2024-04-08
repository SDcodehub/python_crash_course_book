import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A language survey object which is available for each test cases"""
    question = "What is language learnt first?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_atore_single_response(language_survey):
    """Test that a single response is stored properly"""

    # question = "Wha language did you first learn to speak?"
    # language_survey = AnonymousSurvey(question)

    language_survey.store_response('English')

    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """checks the storage of 3 responses"""

    # question = "What is your first language?"

    # language_survey = AnonymousSurvey(question)

    responses = ['English', 'Hindi', 'German']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert  response in language_survey.responses