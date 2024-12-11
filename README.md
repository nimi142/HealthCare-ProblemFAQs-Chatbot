# HealthCare-ProblemFAQs-Chatbot

### Implementation of Chatbot Using NLP

#### Overview  
This project focuses on creating a chatbot that uses **Natural Language Processing (NLP)** to understand user input and provide accurate responses based on predefined intents. The chatbot utilizes the **nltk** library for processing user text, **scikit-learn** for training the model using machine learning algorithms, and **Streamlit** to build a simple web interface for easy user interaction.

#### Features  
- Recognizes various user intents, including greetings, farewells, gratitude, and more.  
- Responds with relevant and pre-defined answers based on user input.  
- Stores and displays conversation history for the user to review.  
- Built in Python using popular libraries for NLP, machine learning, and web development.  

#### Technologies Used  
- **Python**  
- **NLTK** (Natural Language Toolkit)  
- **Scikit-learn** (Machine Learning)  
- **Streamlit** (Web Interface)  
- **JSON** (For storing intents data)  

#### Installation  
1. Install latest version python
4. Install Jupyter Notebook
5. Install NLTK
6. Download NLTK data
7. Install streamlit

#### Usage  
To run the chatbot, use the following command:
python =m streamlit run app.py

Once the application is running, you can start chatting with the bot through the web interface. Type a message in the input box and press Enter to receive a response.

#### Intents Data  
The chatbot's behavior is controlled by the **intents.json** file, which contains different user queries (patterns) and corresponding responses. You can update this file to add new intents or modify existing ones to enhance the chatbot's capability.

#### Conversation History  
All interactions with the chatbot are saved in a **chat_log.csv** file. You can view the history of your conversations through the "Conversation History" option in the sidebar of the web interface.

#### Contributing  
Contributions are welcome! If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.

#### License  
This project is licensed under the **MIT License**. For more details, please refer to the LICENSE file in the repository.

#### Acknowledgments  
- **NLTK** for natural language processing.  
- **Scikit-learn** for implementing machine learning models.  
- **Streamlit** for creating the web interface.

---

This template provides a clean and easy-to-follow explanation of your project, highlighting key features and steps for installation and usage. You can replace `<repository-url>` and `<repository-directory>` with your actual information and modify sections as needed for further clarity or customization.
