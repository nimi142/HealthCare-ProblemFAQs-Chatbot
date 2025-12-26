import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
 
#file_path = r'C:\Users\nami0\OneDrive\Documents\Chatbot\intents.json'
file_path = os.path.abspath("./intents.json") 
with open(file_path, "r") as file:
    intents = json.load(file)

#print(intents)  # Check the structure of the loaded JSON

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)







# training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        
counter = 0

def main():
    global counter

    st.title("**Medical Assistance Chatbot** :hospital: ")

# To change the colour of title 
#   st.markdown(
#        "<h1 style='color:#28B463;'>Medical Assistance Chatbot 🏥</h1>",
#       unsafe_allow_html=True
#   )

       
    # Create a sidebar menu with options
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Home Menu
    if choice == "Home":
        st.caption("Your virtual assistant for quick medical guidance 🧑‍⚕️🩺")
        st.text("Ready to get started? Type your question below and begin the conversation!")

        # Check if the chat_log.csv file exists, and if not, create it with column names
        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("You:", key=f"user_input_{counter}")

        st.button("Ask")

        if user_input:

            # Convert the user input to a string
            user_input_str = str(user_input)

            response = chatbot(user_input)
            st.text_area("Chatbot:", value=response, height=170, max_chars=None, key=f"chatbot_response_{counter}")

            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")

            # Save the user input and chatbot response to the chat_log.csv file
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input_str, response, timestamp])

    elif choice == "Conversation History":
    # Display the conversation history in a collapsible expander
        st.header("Conversation History")

        # Check if the 'chat_log.csv' file exists before attempting to read it
        if os.path.exists('chat_log.csv') and os.path.getsize('chat_log.csv') > 0:
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip the header row
                for row in csv_reader:
                    st.text(f"User: {row[0]}")
                    st.text(f"Chatbot: {row[1]}")
                    st.text(f"Timestamp: {row[2]}")
                    st.markdown("---")
        else:
            st.warning("No conversation history found. Start a chat to see the history here!")


    elif choice == "About":
        st.write("The goal of this project is to create a chatbot that can understand and respond to user input based on intents. The chatbot is built using Natural Language Processing (NLP) library and Logistic Regression, to extract the intents and entities from user input. The chatbot is built using Streamlit, a Python library for building interactive web applications.")

        st.subheader("Project Overview:")

        st.write("""
        The project is divided into two key components:  

        1. **Chatbot Training**:  
            - NLP techniques are applied to process user queries.  
            - The chatbot is trained using a Logistic Regression algorithm on labeled intents and entities to understand and respond accurately to medical FAQs.  

        2. **Chatbot Interface Development**:  
            - The **Streamlit** web framework is used to create a user-friendly, web-based chatbot interface.  
            - The interface enables users to input text queries and receive contextually relevant responses from the chatbot in real-time.           
        """)

        st.subheader("Dataset:")

        st.write("""
        The dataset for this project consists of a structured collection of labeled intents and entities, stored in a list format.  

        - **Intents**: Represent the purpose behind the user's query (e.g., *"Cuts"*, *"Abrasions"*, *"Stings"*).  
        - **Entities**: Extracted keywords or phrases from user input (e.g., *"What to do if cuts?"*, *"Which medicine to apply for abrasions?"*, *"Stings"*).  
        - **Text**: The raw user input provides to the chatbot.  
        """)

        st.subheader("Chatbot Interface:")

        st.write("""
        The chatbot interface is developed using **Streamlit**, featuring:  
        - A text input box for users to enter their queries.  
        - A chat window to display the chatbot's responses.  
        The interface utilizes the trained model to process user inputs and provide appropriate responses in real-time.  
        """)

        st.subheader("Project Summary:")

        st.write("This project involves creating a chatbot capable of interpreting and responding to user queries based on predefined intents. It employs **NLP** and **Logistic Regression** for training and uses **Streamlit** to develop the user interface. The chatbot can be enhanced further by expanding the dataset, incorporating advanced NLP methods, and leveraging deep learning algorithms.  ")

if __name__ == '__main__':
    main()