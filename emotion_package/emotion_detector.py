import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_predictor(text_to_analyze):
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)
    except requests.exceptions.RequestException:
        return None

    if response.status_code != 200:
        return None

    emotions = response.json()["emotionPredictions"][0]["emotion"]

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": max(emotions, key=emotions.get),
    }

