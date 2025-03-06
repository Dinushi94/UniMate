from flask import Flask, request, jsonify
import nltk
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

# Sample responses for common queries
faq_responses = {
    "admissions": "You can check the admission details at https://sliit.lk/admissions",
    "courses": "Visit https://courseweb.sliit.lk to check your registered courses.",
    "fees": "Fee payment details are available at https://sliit.lk.",
    "location": "SLIIT is located at Malabe, Sri Lanka."
}

@app.route('/')
def home():
    return "Welcome to the Unimate Chatbot API! Use /chat to send queries."


def process_query(user_input):
    doc = nlp(user_input.lower())
    for keyword in faq_responses.keys():
        if keyword in user_input:
            return faq_responses[keyword]
    return "I'm sorry, I couldn't find an answer. Please check https://sliit.lk for more info."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get("message", "")
    response = process_query(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
