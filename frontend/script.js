async function processText() {
    const inputText = document.getElementById("inputText").value;
    const action = document.getElementById("action").value;
    const response = await fetch(`http://127.0.0.1:5000/${action}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText })
    });

    const result = await response.json();
    document.getElementById("outputText").value = result.output;
}
