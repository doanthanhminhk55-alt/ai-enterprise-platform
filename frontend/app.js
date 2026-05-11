const API_BASE = "http://127.0.0.1:8000";

const sessionId = "minh-session";

async function uploadPDF() {

    const fileInput =
        document.getElementById("pdfFile");

    const file = fileInput.files[0];

    if (!file) {

        alert("Please choose a PDF");

        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    document.getElementById(
        "uploadStatus"
    ).innerText = "Uploading...";

    const response = await fetch(
        `${API_BASE}/upload`,
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();

    document.getElementById(
        "uploadStatus"
    ).innerText = data.message;
}

function addMessage(role, content) {

    const chatBox =
        document.getElementById("chatBox");

    const div =
        document.createElement("div");

    div.classList.add(
        "message",
        role
    );

    div.innerText = content;

    chatBox.appendChild(div);

    chatBox.scrollTop =
        chatBox.scrollHeight;
}

async function sendMessage() {

    const input =
        document.getElementById(
            "questionInput"
        );

    const question = input.value;

    if (!question) return;

    addMessage("user", question);

    input.value = "";

    const chatBox =
        document.getElementById("chatBox");

    const aiDiv =
        document.createElement("div");

    aiDiv.classList.add(
        "message",
        "assistant"
    );

    aiDiv.innerText = "";

    chatBox.appendChild(aiDiv);

    const response = await fetch(
        `${API_BASE}/chat-stream?question=${encodeURIComponent(question)}`
    );

    const reader =
        response.body.getReader();

    const decoder =
        new TextDecoder();

    while (true) {

        const { done, value } =
            await reader.read();

        if (done) break;

        const chunk =
            decoder.decode(value);

        aiDiv.innerText += chunk;

        chatBox.scrollTop =
            chatBox.scrollHeight;
    }
}

document
    .getElementById("questionInput")

    .addEventListener(
        "keypress",

        function (event) {

            if (event.key === "Enter") {

                sendMessage();
            }
        }
    );