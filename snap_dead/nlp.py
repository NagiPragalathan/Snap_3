import spacy
import requests
import wikipedia

# it's gives the subject of the content

nlp = spacy.load('en_core_web_sm')

def answer_question(question):
    doc = nlp(question)

    # Extract subject and object
    subject = None
    obj = None
    for token in doc:
        if token.dep_ == 'nsubj':
            subject = token.text
        elif token.dep_ == 'dobj':
            obj = token.text
    print("Subject",subject,obj)
    # Extract entities
    entities = [ent.text for ent in doc.ents]

    # Join all parts into search query
    parts = [part for part in [subject, obj] if part is not None]
    search_query = " ".join(entities + parts).strip()
    print("search_query, ",search_query)
    # Search Wikipedia for page
    page = wikipedia.page(search_query)

    # Return summary of page
    return page.summary

# print(answer_question("who is pm of india"))

import requests
from bs4 import BeautifulSoup

def get_wikipedia_answer(question):
    # Clean the question string
    question = question.strip().replace(' ', '_')

    # Send a GET request to the Wikipedia API
    url = f'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles={question}'
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()
    pages = data['query']['pages']
    page_id = next(iter(pages))
    extract = pages[page_id]['extract']

    # Extract the first paragraph as the answer
    soup = BeautifulSoup(extract, 'html.parser')
    answer = soup.get_text().split('\n')[0]

    return answer
# print(get_wikipedia_answer("who is pm of india ?"))


import wikipedia

def answer_question(question):
    try:
        page = wikipedia.page(question)
        summary = page.summary
        return summary.split('\n')[0]  # return the first paragraph
    except wikipedia.exceptions.PageError:
        return "I'm sorry, I don't know the answer to that."
    except wikipedia.exceptions.DisambiguationError:
        return "There are multiple pages with that name. Can you please be more specific?"

# Example usage
question = "Who is the current president of the United States?"
answer = answer_question(question)
print(answer)

print(answer_question("who is pm of india"))