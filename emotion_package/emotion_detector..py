import requests
import json


def emotion_predictor(text_to_analyze):
    url = "https://watson-api-endpoint/emotion"
    params = {"text": text_to_analyze}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    result = response.json()

    return {
        "anger": result["emotion"]["anger"],
        "disgust": result["emotion"]["disgust"],
        "fear": result["emotion"]["fear"],
        "joy": result["emotion"]["joy"],
        "sadness": result["emotion"]["sadness"],
        "dominant_emotion": max(
            result["emotion"],
            key=result["emotion"].get
        ),
    }

