🧠 Multimodal AI Agent

🚀 Text + Image Understanding using AI

<p align="center">
  <img src="https://img.shields.io/badge/AI-Multimodal-blueviolet?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Streamlit-Deployed-success?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-Project-yellow?style=for-the-badge"/>
</p>---

🌐 🔗 Live Demo

👉 Try it here:
🔗 https://multimodalagent-gxum3ml6xovzb5vdaeucr9.streamlit.app

---

✨ Overview

This project is a Multimodal AI Agent that can understand both:

- 🖼️ Images
- 💬 Text

It combines computer vision + language understanding to generate intelligent responses.

---

🧠 How It Works

Image → BLIP → Caption  
Text + Caption → Prompt  
Prompt → LLM → Final Answer

---

⚙️ Tech Stack

- 🐍 Python
- 🎯 Streamlit (Frontend + Deployment)
- 🖼️ BLIP (Image Captioning)
- 🤖 LLaMA (via API)
- ☁️ Streamlit Cloud

---

📸 Features

✅ Upload any image
✅ Ask questions about the image
✅ AI understands context
✅ Clean UI
✅ Deployed and accessible online

---

🚀 Run Locally

git clone https://github.com/YOUR_USERNAME/Multimodal_Agent.git
cd Multimodal_Agent

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

export GROQ_API_KEY="your_api_key"

streamlit run app.py

---

🔐 Environment Variables

Create a ".env" or use:

GROQ_API_KEY=your_api_key

---

📂 Project Structure

multimodal-agent/
│
├── app.py
├── model/
│   ├── blip.py
│   └── llm.py
├── utils/
│   └── prompt.py
├── requirements.txt
└── README.md

---

🌟 Future Improvements

- 🔥 Chat history memory
- 🎤 Voice input support
- 🧠 Better multimodal models (LLaVA / Gemini)
- 🎨 UI enhancements

---

👩‍💻 Author

Shalini Saurav
🚀 AI | Data Science | Builder

---

⭐ Show Your Support

If you like this project:
👉 Star ⭐ the repo
👉 Share it

---

<p align="center">
  💡 "Building intelligent systems that understand the world like humans."
</p>
