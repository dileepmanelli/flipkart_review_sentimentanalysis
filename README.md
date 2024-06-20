# flipkart_review_sentimentanalysis
#Flipkart Sentiment Analysis using LSTM
#Overview
This project performs sentiment analysis on Flipkart product reviews using Long Short-Term Memory (LSTM) networks. The model is trained to classify the sentiment of reviews into positive, negative, or neutral categories. The application is deployed as a web service on an AWS EC2 instance, allowing users to input text reviews and receive sentiment predictions in real-time.

#Features
LSTM Model: Utilizes LSTM neural networks for their ability to capture context and dependencies in sequential data, making them suitable for natural language processing tasks like sentiment analysis.
Web Application: Provides a user-friendly interface where users can input text reviews.
Real-time Prediction: Delivers sentiment predictions instantaneously upon submission of reviews.
AWS EC2 Deployment: Hosted on an AWS EC2 instance for scalability and reliability.
#Project Structure
///

├── app/
│   ├── templates/
│   │   ├── index.html         # HTML template for the web interface
│   ├── static/
│   │   ├── styles.css         # CSS styles for the web interface
│   ├── app.py                 # Flask application for handling web requests
│   ├── lstm_model.py          # LSTM model for sentiment analysis
│   ├── utils.py               # Utility functions for data preprocessing and model prediction
├── data/
│   ├── reviews.csv            # Dataset containing Flipkart reviews (sample)
├── model/
│   ├── lstm_sentiment_model.h5# Pre-trained LSTM model weights
├── README.md                  # This file, containing project information and setup instructions
├── requirements.txt           # Python dependencies
///

#Setup Instructions
Prerequisites
Python 3.x
AWS EC2 instance (or similar server hosting service)
Basic understanding of Flask web framework
Steps to Deploy
Clone the repository:

git clone https://github.com/yourusername/flipkart-sentiment-analysis.git
cd flipkart-sentiment-analysis
Install dependencies:

pip install -r requirements.txt
Upload model weights:
Transfer lstm_sentiment_model.h5 to your AWS EC2 instance. Place it in the model/ directory.

Run the Flask application:

python app/app.py
This will start the Flask development server.

Access the web application:
Open a web browser and navigate to http://your-ec2-instance-ip:5000 (replace your-ec2-instance-ip with your actual EC2 instance IP address). You should see the web interface for entering reviews.

#Usage
Enter a review: Type or paste a review into the input box on the web interface.
Submit: Click the "Predict Sentiment" button to receive the sentiment prediction.
View result: The sentiment prediction (positive, negative, or neutral) will be displayed below the input box.
Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or additional features.

#License
This project is licensed under the MIT License - see the LICENSE file for details.

#Acknowledgments
Inspired by the need to analyze sentiment from Flipkart reviews using deep learning techniques.
