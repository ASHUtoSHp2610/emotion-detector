from flask import Flask, render_template, request
from emotion_package import emotion_predictor

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Renders the initial HTML input page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get input text from the HTML form
    user_text = request.form.get('user_input')

    if not user_text:
        return render_template('index.html', error="Please enter some text.")

    # 2. Run the text through the emotion predictor
    result = emotion_predictor(user_text)

    if result is None or result['dominant_emotion'] is None:
        return render_template('index.html', error="Error calling the AI service.", original_text=user_text)

    output_text = (
        f"Dominant emotion: {result['dominant_emotion']} "
        f"(anger={result['anger']}, disgust={result['disgust']}, "
        f"fear={result['fear']}, joy={result['joy']}, sadness={result['sadness']})"
    )

    # 3. Return the result back to the web page
    return render_template('index.html', prediction_text=output_text, original_text=user_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
