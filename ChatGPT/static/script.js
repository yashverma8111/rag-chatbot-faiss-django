const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");

function sendMessage() {
    const message = userInput.value.trim();

    if (message === "") return;

    // Add user message
    addMessage(message, "user");

    userInput.value = "";

    // Simulate bot reply
    setTimeout(() => {
        addMessage("This is a demo response.", "bot");
    }, 1000);
}

function addMessage(text, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);
    messageDiv.textContent = text;

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message on Enter key
userInput.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});