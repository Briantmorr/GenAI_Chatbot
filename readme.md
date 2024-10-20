#  Comment by Prema Mallikarjunan 10/20/2024
Chatbot UI Instructions
Prerequisites
Before running the chatbot UI, ensure that you have the following installed:
•	Python 3.x
•	Required Python packages (see requirements.txt for a complete list)
You can install the necessary packages using the following command:
pip install -r requirements.txt
1. Clone the Repository
Clone this repository to your local machine using the following command:
git clone <repository-url>
2. Navigate to the Project Directory
Change your directory to the project folder:
cd <project-directory>
3. Prepare Your Dataset
•	Make sure you have the training data file (e.g., train-v1.1.json) located in the same directory as the app.py file. This file should contain the data formatted in JSON, with questions and contexts.
4. Run the Notebook
Open your Jupyter Notebook or Google Colab.
•	If using Google Colab, upload your files (like train-v1.1.json, index.html, and app.py) to the Colab environment.
•	Ensure you set the paths correctly in your app.py file for loading the index.html.
5. Execute the Code
Run the following code in a notebook cell to start the Flask app:
python
!python app.py
6. Access the Chatbot UI
Once the Flask server is running, you will see output similar to this:
 * Running on http://127.0.0.1:5000
If you are running in Google Colab, you will also see a ngrok link that you can use to access the chatbot UI from your browser:
 * ngrok tunnel "NgrokTunnel: "https://<your-ngrok-link>" -> "http://localhost:5000"
Click on the provided ngrok link to open the chatbot UI in your web browser.
7. Interact with the Chatbot
In the chatbot UI, you can type your questions related to the content in your dataset and get responses. The chatbot will utilize the fine-tuned model to provide answers based on the context provided in your training data.
8. Stopping the Server
To stop the server, you can interrupt the execution of the cell running the Flask app (e.g., by pressing Ctrl + C in a terminal or stopping the execution in Colab).











#  Comment by Prema Mallikarjunan 9/30/2024
Created a new folder "WebInterface" for the frontend.
-  app.py file was added for generating a response, and returns the answer on the same page.
-  a separate template file "Index.html" was created to ask a question and answer and the conversation history.
-  used 'Flask" library for running this web interface.

-  EDA 4
  - loaded both datasets train-v1.1.json and dev-v1.1.json into Python using json.load().
  - Extracting Contexts: Contexts (passages of text) are extracted from both datasets and stored in a list called contexts.
  - Combining Contexts: The contexts from both datasets are combined into one list, allowing the chatbot to use both train and dev contexts.
  - Find Best Context (Simplified): Currently, the script selects the first context for simplicity, but this can be improved using keyword matching or semantic similarity.
  - Running the Chatbot: The chatbot takes a user’s question, finds a context, and returns an answer using Hugging Face's transformers library.
  - Finally, created many visuals:
  -     1. Distribution of Context Lengths
        2. Distribution of Question Lengths
        3. Distribution of Answer Lengths
        4. Distribution of Answer Start Positions in Context
        5. Comparison of Context Lengths and Answer Lengths (Scatter Plot)
        6. Word Cloud of Contexts
        7. Most Common First Words in Questions

#  Comment by Prema Mallikarjunan 9/20/2024
#  EDA 1 
  -   EDA1 uses the dev-v1.1.json file. 
  -   Load the Data: I'll parse the JSON structure and convert it into a pandas DataFrame to explore the different elements.
  -   Initial Inspection: We'll examine the basic structure of the dataset, such as the titles, contexts, questions, and answers.
  -   Context, Question, and Answer Distribution: We'll analyze the distribution of text lengths to understand the variation in context, question, and answer lengths.

I've displayed the initial structure of the dev-v1.1.json data for you. The dataset includes columns for titles, contexts, questions, answers, and answer start positions. Now let's proceed with a deeper analysis:

Context Length Distribution: Analyze the lengths of the contexts.
Question Length Distribution: Analyze the lengths of the questions.
Answer Length Distribution: Analyze the lengths of the answers.
Missing Values Check: Verify if there are any missing or null values.

For visualizing the length distributions of context, questions, and answers, use matplotlib library.  The code also display the summary statistics for context length, question length, and answer length, as well as checking for missing values in your DataFrame.

#  EDA 2
#  Example Python script to Build the QA Chatbot Using SQuAD

  -  The pre-trained BERT model for question-answering using the "pipeline" library.
  -  Pipeline: We use Hugging Face’s pipeline function with "question-answering", which loads a pre-trained QA model (like BERT or DistilBERT) to answer questions based on context.
  -  Context: You provide a text passage (context) from which the chatbot will search for answers.
  -  User Input: The chatbot takes user questions in a loop and returns the answer using the QA model.
  -  Exit Condition: The loop breaks when the user types "exit".
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Getting Started
## Overview
This project focuses on designing and implementing an advanced generative chatbot using state-of-the-art architectures and techniques. The chatbot is capable of carrying out multi-turn conversations, adapting to context, and handling a variety of topics.

## Project Goal
- Objective: Build a generative chatbot that can engage in coherent and context-aware conversations with users.
- Output: A working chatbot accessible via a Jupyter Notebook and a web interface.

## Dataset
- Stanford Question Answering Dataset (SQuAD): A comprehensive dataset consisting of questions posed by crowdworkers on a set of Wikipedia articles, paired with the corresponding answers in the text.

## How to Use the Chatbot
#### Access via Notebook
1. Clone the repository:
``` 
git clone https://github.com/briantmorr/GenAI_Chatbot.git
```

2. Run the notebook:
```
jupyter notebook chatbot.ipynb
```
