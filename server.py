"""Module providing a server routes for detecting emotions."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def detect_emotion():
    """Function gets detected emotion."""
    text_input = request.args.get("textToAnalyze")
    res = emotion_detector(text_input)
    if res["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    emotions = {k: v for k, v in res.items() if k != "dominant_emotion"}
    emotions_str = ", ".join([f'"{k}": {v}' for k, v in emotions.items()])
    return (
        f"For the given statement, the system response is {emotions_str}.",
        f'The dominant emotion is {res["dominant_emotion"]}.',
    )


@app.route("/")
def render_index():
    """Render home page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
