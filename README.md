

# 🚀 Streamlit LLM App (Groq API Integration)

A simple yet powerful Streamlit application that integrates the **Groq API** to build an interactive LLM-powered chatbot or data app.
This project demonstrates how to securely use environment variables, deploy Streamlit apps, and interact with Groq models.

---

## 🧠 Features

* Streamlit-based web UI
* Integration with **Groq LLM API**
* Environment variable handling with `.env`
* Modular, easy-to-extend code
* Compatible with **local and cloud deployments (Streamlit Cloud)**

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** – frontend & UI framework
* **Groq API** – LLM engine
* **python-dotenv** – for secure API key management

---

## 📂 Project Structure

```
📁 your_project/
 ├── app.py                # Main Streamlit app
 ├── .env                  # Environment file (your API key)
 ├── requirements.txt      # Dependencies
 ├── README.md             # Project documentation
 └── .gitignore            # Prevents .env & cache files from being committed
```

---

## ⚙️ Installation

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file

Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_actual_api_key_here
```

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment on Streamlit Cloud

1. Push your code to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Select your repository.
4. In **Advanced settings**, add your environment variable:

   * Key: `GROQ_API_KEY`
   * Value: `your_actual_api_key`
5. Deploy


## LIVE DEMO 

[ava](https://llmprojects1-b2amtcgdf94fsmtfmxsavv.streamlit.app/)

---

## ❤️ Credits

Developed with love, coffee, and chaos by **Vivek** 🧠⚡
Powered by **Streamlit** and **Groq**.

---

