# Unimate Chatbot - Student Support Assistant

Unimate is a chatbot designed to assist students with common administrative queries, course information, and campus events using **Natural Language Processing (NLP)** with **Python, Flask, NLTK, and spaCy**.

---
## 🚀 Features
- Answer common student queries about courses, events, and administration
- Uses **NLTK** and **spaCy** for natural language processing
- API-based interaction using **Flask**
- Easily expandable with more FAQs and integrations

---
## 📌 Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/unimate-chatbot.git
cd unimate-chatbot
```

### 2️⃣ **Create a Virtual Environment** (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ **Install Required Libraries**
```sh
pip install flask flask-cors nltk spacy
python -m spacy download en_core_web_sm
```

---
## 🛠️ Running the Chatbot
```sh
python app.py
```
If successful, you should see output like:
```sh
 * Running on http://127.0.0.1:5000
```

---
## 🔥 API Usage

### 📌 **1. Test Using Curl** (For Linux/macOS)
```sh
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Tell me about courses"}'
```

### 📌 **2. Test Using PowerShell** (For Windows)
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/chat" `
    -Method POST `
    -Headers @{"Content-Type"="application/json"} `
    -Body '{"message": "Tell me about courses"}'
```

### 📌 **3. Test Using Postman**
- Open **Postman**
- Set method to **POST**
- URL: `http://127.0.0.1:5000/chat`
- Go to **Body → Raw**
- Select **JSON format**
- Enter:
```json
{
  "message": "Tell me about courses"
}
```
- Click **Send**

---
## 🏗️ Project Structure
```
📂 unimate-chatbot/
│── app.py  # Flask backend
│── chatbot.py  # NLP logic using NLTK & spaCy
│── requirements.txt  # Dependencies
│── README.md  # Documentation
```

---
## 🔮 Future Enhancements
- Database integration for dynamic responses
- Voice input support
- Deploying to AWS/GCP for real-world usage

---
## 📜 License
This project is open-source under the **MIT License**.

---
## 🤝 Contributing
Pull requests are welcome! Feel free to suggest improvements or report bugs.

---
## 🔗 References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [NLTK Documentation](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/)
- [SLIIT Official Website](https://sliit.lk)

