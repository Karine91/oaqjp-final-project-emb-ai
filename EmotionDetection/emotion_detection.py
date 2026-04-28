import requests, json


def emotion_detector(text_input):
    text_to_analyze = text_input
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    data = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    res = requests.post(url, json=data, headers=headers)
    formatted = json.loads(res.text)
    emotions = formatted["emotionPredictions"][0]["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    scores_dict = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }
    dominant_emotion = max(scores_dict, key=scores_dict.get)
    return {**scores_dict, "dominant_emotion": dominant_emotion}
