from flask import Flask, request, jsonify
from emotion_package import emotion_predictor

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def get_emotion():
    text = request.args.get("textToAnalyze")

    if not text:
        return "Error: No text provided", 400

    result = emotion_predictor(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
    