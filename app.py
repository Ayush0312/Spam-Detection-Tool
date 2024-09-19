from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the saved model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Result route to handle form POST
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # Get the message from the form
        message = request.form['message']

        # Transform the message using the vectorizer
        message_transformed = vectorizer.transform([message])

        # Predict whether it's spam or not
        prediction = model.predict(message_transformed)[0]

        # Set the prediction result and corresponding CSS class
        if prediction == 1:
            result_text = "Spam"
            css_class = "spam"
        else:
            result_text = "Not Spam"
            css_class = "not-spam"

        # Pass the result to the result.html template
        return render_template('result.html', input_text=message, prediction=result_text, css_class=css_class)

if __name__ == "__main__":
    app.run(debug=True)
