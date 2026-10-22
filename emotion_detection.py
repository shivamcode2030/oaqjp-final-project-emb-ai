"""Emotion detection using IBM Watson NLP."""

import json

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def _empty_result():
    """Return the standard result for invalid input."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze):
    """Detect emotions in text using the Watson NLP EmotionPredict service."""
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return _empty_result()

    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        URL,
        json=payload,
        headers=HEADERS,
        timeout=30,
    )

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
