const toggleAiBtn = document.getElementById("toggle-ai-btn");
document.querySelector("#send-btn").addEventListener("click", async () => {
  const csrfTokenChat = document.querySelector(
    'meta[name="csrf-token"]'
  ).content;
  const chatBox1 = document.querySelector(".chat-output");
  const input = document.querySelector("#chat-input");
  const message = input.value.trim();
  if (!message) return;

  // Add user's message to chat
  chatBox1.innerHTML += `<div class="user-msg">${message}</div>`;
  input.value = "";

  // Send to Flask backend
  sendToBot(message, (action = null), csrfTokenChat);
});

function addMessage(text, sender) {
  const chatBox1 = document.querySelector(".chat-output");
  const msg = document.createElement("div");
  msg.classList.add(sender === "bot" ? "bot-msg" : "user-msg");
  msg.textContent = text;
  chatBox1.appendChild(msg);
  chatBox1.scrollTop = chatBox1.scrollHeight;
}

async function sendToBot(message, action = null, csrfToken) {
  const response = await fetch("/chatbot", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ message, action }),
  });

  const data = await response.json();
  addMessage(data.reply, "bot");
}

document.querySelectorAll(".chat-options button").forEach((btn) => {
  btn.addEventListener("click", () => {
    const csrfTokenChat = document.querySelector(
      'meta[name="csrf-token"]'
    ).content;
    const action = btn.dataset.action;
    addMessage(btn.textContent, "user");
    sendToBot(null, action, csrfTokenChat);
  });
});

  // 🔹 Toggle AI button
toggleAiBtn.addEventListener("click", () => {
  const csrfTokenChat = document.querySelector(
    'meta[name="csrf-token"]'
  ).content;
  const mode = toggleAiBtn.getAttribute("data-mode");

  if (mode === "off") {
    // Start AI mode
    toggleAiBtn.textContent = "❌ Exit AI";
    toggleAiBtn.setAttribute("data-mode", "on");
    addMessage("Starting AI assistant...", "user");
    sendToBot(null, "generative_ai", csrfTokenChat);
  } else {
    // Exit AI mode
    toggleAiBtn.textContent = "🤖 Start AI";
    toggleAiBtn.setAttribute("data-mode", "off");
    addMessage("Exiting AI assistant...", "user");
    sendToBot(null, "exit_ai", csrfTokenChat);
  }
});

