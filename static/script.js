function checkURL() {
    let url = document.getElementById("urlInput").value;
    let resultElement = document.getElementById("result");
    let explanationElement = document.getElementById("explanation");

    if (!url) {
        resultElement.innerHTML = "Please enter a URL.";
        explanationElement.innerHTML = "";
        return;
    }

    // Show loading animation
    resultElement.innerHTML = "Checking... <span class='loading'></span>";
    explanationElement.innerHTML = "";

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultElement.innerHTML = "Error: " + data.error;
            explanationElement.innerHTML = "";
        } else {
            resultElement.innerHTML = `<strong>Result:</strong> <span style="color: ${data.prediction === "Phishing" ? "red" : "green"}">${data.prediction}</span>`;
            
            let explanationText = data.reasons ? data.reasons.map(reason => `• ${reason}`).join("<br>") : "No explanation available.";
            explanationElement.innerHTML = `<strong>Why?</strong><br>${explanationText}`;
        }
    })
    .catch(error => {
        resultElement.innerHTML = "Error checking URL.";
        explanationElement.innerHTML = "";
        console.error("Error:", error);
    });
}
