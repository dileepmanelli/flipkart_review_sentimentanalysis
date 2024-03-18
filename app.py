from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load(r"C:\Users\dilee\Downloads\Flipkart_review\best_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        sentiment = model.predict([review])[0]
        sentiment_label = "Positive" if sentiment == 1 else "Negative"
        return render_template('result.html', review=review, sentiment=sentiment_label)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9000)
