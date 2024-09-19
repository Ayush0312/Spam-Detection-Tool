Spam Detection Tool

This is a simple tool to help detect spam messages using machine learning. You can paste any text into a web page, and it will tell you if it's "Spam" or "Not Spam."
Features

    Easy to Use: Just paste your text and get results instantly.
    Machine Learning: Uses a trained model to detect spam.
    Quick Results: Fast, real-time detection.

How to Install

Follow these steps to run it on your computer:
Clone the Repository:

bash

git clone https://github.com/your-username/Spam-Detection-Tool.git
cd Spam-Detection-Tool

Create a Virtual Environment:

bash

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

Install Dependencies:

bash

pip install -r requirements.txt

Run the App:

bash

python app.py

Now, open your browser and go to http://localhost:5000.
How to Use

    Go to the website (http://localhost:5000).
    Paste your text in the input box.
    Hit submit and see if it’s spam or not!

Project Files

    app.py: The main app code.
    model.pkl: The trained machine learning model.
    vectorizer.pkl: Helps the model understand the text.
    templates/index.html: The webpage template.
    static/styles.css: The webpage design.

Model Info

The tool uses a machine learning model trained to identify spam messages. The model and the vectorizer for processing text are already included in the files (model.pkl and vectorizer.pkl).
Contributing

Want to improve the tool? Feel free to fork the repo and submit a pull request!
