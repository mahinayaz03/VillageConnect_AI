# &nbsp;**VillageConnect AI**



##### Project Overview :



VillageConnect AI is a web-based NLP chatbot designed to assist rural communities by providing quick information about government schemes, healthcare services, utilities, and other essential services. The system uses TF-IDF vectorization and cosine similarity to understand user queries and respond with relevant information.



##### Problem Statement :



Rural citizens often face difficulty accessing structured information about:

* Government schemes
* Healthcare services
* Agricultural support
* Utility services
* Public welfare programs



VillageConnect AI aims to provide an accessible, intelligent chatbot solution to bridge this information gap.





##### Technologies Used :



* Python
* Flask (Web Framework)
* TF-IDF Vectorizer (scikit-learn)
* Cosine Similarity
* HTML + CSS
* Jinja2 Templating
* JSON (Intent storage)
* File Logging System





##### How It Works :



1\. User enters a query through the web interface.

2\. The query is processed using TF-IDF vectorization.

3\. Cosine similarity is calculated between the user query and stored intent patterns.

4\. The most similar intent is selected.

5\. If similarity score is above a confidence threshold (0.4), the corresponding response is returned.

6\. Chat history is stored in memory.

7\. Each conversation is logged with a timestamp in `chat\_log.txt`.





##### Features :



* Intent-based NLP chatbot
* TF-IDF based text processing
* Cosine similarity matching
* Confidence threshold handling
* Real-time chat history display
* Timestamp for each message
* Clear chat functionality
* Automatic logging of user queries and responses
* Responsive web interface





##### Project Structure :



VillageConnect-Advanced/

│

├── app.py

├── chatbot.py

├── data.json

├── chat\_log.txt

├── templates/

│   └── index.html

└── README.md





##### Future Enhancements :



* Integration with live government APIs
* Multi-language support (Tamil, Hindi, etc.)
* Database integration (SQLite/MySQL)
* Admin dashboard for analytics
* Voice input support
* Mobile application version





##### Conclusion :



VillageConnect AI demonstrates the practical implementation of Natural Language Processing using TF-IDF and cosine similarity in a real-world web application environment. It combines AI logic, web development, and data logging into a structured solution aimed at solving real-world rural information accessibility challenges.



