function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const result = document.getElementById("system_response");

    if (!textToAnalyze.trim()) {
        result.textContent = "Invalid text! Please try again!";
        return;
    }

    fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze))
        .then((response) => response.text().then((text) => ({
            ok: response.ok,
            text
        })))
        .then((data) => {
            result.textContent = data.text;
        })
        .catch(() => {
            result.textContent = "Unable to reach the emotion detector.";
        });
}
