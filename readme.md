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
