from flask import Flask, render_template, request
from transformers import pipeline
import json

app = Flask(__name__)

# Load data (contexts) from a dataset (similar to SQuAD or custom dataset)
train_file_path = 'C:/USD/Natural Language Processing and GenAI AAI 520/Final Project/archive/train-v1.1.json'

with open(train_file_path, "r") as train_file:
    train_data = json.load(train_file)

# Extract contexts from the dataset
contexts = []
for article in train_data['data']:
    for paragraph in article['paragraphs']:
        contexts.append(paragraph['context'])  # Add each context to the list

# Initialize the question-answering model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", framework="pt", device=-1)

# Initialize an empty conversation history
conversation_history = []

# Function to find the best matching context based on the question
def find_best_context(question, contexts):
    question_keywords = set(question.lower().split())  # Split the question into keywords
    best_context = None
    max_overlap = 0

    for context in contexts:
        context_words = set(context.lower().split())  # Split the context into words
        overlap = len(question_keywords.intersection(context_words))  # Count matching words
        
        if overlap > max_overlap:
            max_overlap = overlap
            best_context = context

    return best_context if best_context else contexts[0]  # Fallback to the first context if none found

# Define a simple route for the homepage
@app.route('/')
def home():
    return render_template('index.html', conversation=conversation_history)  # Render the web page

# Define a route to handle the chatbot responses
@app.route('/get', methods=['POST'])
def chatbot_response():
    user_question = request.form.get('question', '').strip()  # Get the user's input and strip any extra whitespace

    # Debugging log to check what is submitted
    print(f"Received question: '{user_question}'")

    if not user_question:
        return "Error: Question cannot be empty. Please enter a valid question."

    # Find the best context dynamically based on the question
    best_context = find_best_context(user_question, contexts)

    # Log the selected context for debugging
    print(f"Selected context: '{best_context[:100]}...'")  # Show the first 100 characters of the context

    # Get the answer from the model using the best-matching context
    try:
        result = qa_pipeline(question=user_question, context=best_context)
        print(f"Model response: '{result['answer']}'")  # Log the answer returned by the model

        # Add the question and answer to the conversation history
        conversation_history.append({"question": user_question, "answer": result['answer']})

    except Exception as e:
        print(f"Error during model inference: {str(e)}")
        return "Error: Unable to get a response from the model."

    # Log the updated conversation history
    print(f"Updated conversation history: {conversation_history}")

    # Return the updated conversation history to the template
    return render_template('index.html', conversation=conversation_history)

# Define a route to clear the conversation history
@app.route('/clear', methods=['POST'])
def clear_conversation():
    global conversation_history  # Access the global conversation history variable
    conversation_history = []  # Clear the conversation history
    return render_template('index.html', conversation=conversation_history)  # Return to the main page

if __name__ == "__main__":
    app.run(debug=True)