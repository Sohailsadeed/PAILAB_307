# 📧 Gmail AI Reply – Chrome Extension

An AI-powered Chrome Extension that injects an **“AI Reply”** button into Gmail and automatically generates professional email responses using a Spring Boot backend.

---

## 🚀 Overview

This extension enhances Gmail by:

- Detecting compose/reply windows dynamically
- Injecting a custom AI button into the toolbar
- Extracting original email content
- Sending content to a backend AI API
- Automatically inserting the generated reply into the compose box

---

## 🛠 Tech Stack

**Frontend (Chrome Extension)**
- JavaScript
- DOM Manipulation
- MutationObserver API
- Chrome Extension APIs

**Backend**
- Spring Boot
- REST API (`/api/email/generate`)
- WebClient
- Gemini / LLM API

---

## ⚙️ How It Works

1. `MutationObserver` monitors Gmail DOM.
2. When a compose window appears, the extension injects the **AI Reply** button.
3. On click:
   - Email content is extracted using Gmail selectors.
   - POST request sent to:
     ```
     http://localhost:8080/api/email/generate
     ```
   - Backend generates AI reply.
   - Reply is inserted into Gmail’s editable textbox.

---

## 🔧 Setup

### 1️⃣ Start Backend
Ensure Spring Boot server is running on:

```
http://localhost:8080
```

### 2️⃣ Load Extension

1. Open `chrome://extensions/`
2. Enable **Developer Mode**
3. Click **Load unpacked**
4. Select the project folder

---

## 📌 Key Implementation Highlights

- Dynamic UI injection inside Gmail
- Real-time DOM observation using `MutationObserver`
- Robust email content extraction using multiple selectors
- Async API integration with error handling
- Automatic reply insertion using `execCommand`
  
---

⭐ If you found this project interesting, consider giving it a star!
