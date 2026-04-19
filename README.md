<div align="center">

```
╔╦╗╦ ╦╦ ╔╦╗╦╔╦╗╔═╗╔╦╗╔═╗╦  
║║║║ ║║  ║ ║║║║║ ║  ║║╠═╣║  
╩ ╩╚═╝╩═╝╩ ╩╩ ╩ ╚═╝═╩╝╩ ╩╩═╝
        AI  AGENT             
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=A855F7&center=true&vCenter=true&width=600&lines=Sees+Images.+Understands+Text.+Thinks+Like+You.;Powered+by+BLIP+%2B+LLaMA+3.3;Built+by+Shalini+Saurav+%F0%9F%9A%80" alt="Typing SVG" />

<br/>

[![Live Demo](https://img.shields.io/badge/🌐_LIVE_DEMO-Try_it_Now_→-a855f7?style=for-the-badge&labelColor=1a0533)](https://multimodalagent-gxum3ml6xovzb5vdaeucr9.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-F55036?style=for-the-badge)](https://groq.com)
[![BLIP](https://img.shields.io/badge/BLIP-Vision_Model-10b981?style=for-the-badge)](https://huggingface.co/Salesforce/blip-image-captioning-large)

<br/>

> *"What if AI could look at an image and talk about it like a human?"*
> **That's exactly what this does.**

</div>

---

## 🧠 The Idea

Most AI is either *good at text* or *good at images* — rarely both.

This agent bridges that gap. Upload any image, ask any question, and watch it think through **vision + language together** — like a human would.

```
      You upload an image  +  You ask a question
               │                      │
               ▼                      ▼
         ┌──────────┐          ┌────────────┐
         │   BLIP   │          │  Your Text │
         │ (Vision) │          │   Query    │
         └────┬─────┘          └─────┬──────┘
              │                      │
              ▼                      ▼
         📝 Caption ────────▶ 🧩 Combined Prompt
                                      │
                                      ▼
                              ┌───────────────┐
                              │  LLaMA 3.3    │
                              │  via Groq ⚡  │
                              └───────┬───────┘
                                      │
                                      ▼
                              💬 Intelligent Answer
```

---

## ✨ What Makes It Special

<table>
<tr>
<td width="50%">

**🖼️ Vision Understanding**
Upload any image — photos, diagrams, screenshots, charts — and the agent understands what's in it before you even ask.

</td>
<td width="50%">

**💬 Natural Language Q&A**
Ask follow-up questions in plain English. No special syntax. No prompting tricks. Just talk.

</td>
</tr>
<tr>
<td width="50%">

**⚡ Groq-Powered Speed**
LLaMA 3.3 70B running on Groq's LPU chips means answers arrive in under 2 seconds — not 20.

</td>
<td width="50%">

**☁️ Live & Deployed**
Not just a local demo. Actually deployed on Streamlit Cloud and accessible from anywhere in the world.

</td>
</tr>
</table>

---

## 🏗️ Tech Stack

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Frontend  ──────────────────────────  Streamlit           │
│   Vision    ──────────────────────────  BLIP (Salesforce)   │
│   Language  ──────────────────────────  LLaMA 3.3 70B       │
│   Inference ──────────────────────────  Groq API ⚡         │
│   Language  ──────────────────────────  Python 3.10+        │
│   Hosting   ──────────────────────────  Streamlit Cloud     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Layer | Technology | Why |
|-------|-----------|-----|
| 🖼️ Image Captioning | BLIP (Salesforce) | State-of-the-art vision-language model |
| 🤖 LLM | LLaMA 3.3 70B | Open-source, powerful, free |
| ⚡ Inference | Groq API | 10x faster than standard GPU inference |
| 🎨 UI | Streamlit | Fast to build, beautiful to use |
| ☁️ Deploy | Streamlit Cloud | Free, instant, shareable |

---

## 📂 Project Structure

```
multimodal-agent/
│
├── 📄 app.py                 ← main streamlit app + UI
│
├── 📂 model/
│   ├── 🖼️  blip.py           ← image captioning pipeline
│   └── 🤖  llm.py            ← groq + llama inference
│
├── 📂 utils/
│   └── 🧩  prompt.py         ← prompt builder (caption + query)
│
├── 📄 requirements.txt       ← all dependencies
├── 📄 .env                   ← GROQ_API_KEY (don't commit!)
└── 📄 README.md
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/Multimodal_Agent.git
cd Multimodal_Agent

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your API key
echo "GROQ_API_KEY=your_api_key_here" > .env

# 5. Launch 🚀
streamlit run app.py
```

> 🔑 Get your **free** Groq API key → [console.groq.com](https://console.groq.com)

---

## 🔐 Environment Variables

```env
GROQ_API_KEY=your_groq_api_key_here
```

For Streamlit Cloud deployment — add this in **Settings → Secrets** (not in `.env` file).

---

## 🌟 Roadmap

- [x] 🖼️ Image upload + captioning
- [x] 💬 Text Q&A on images  
- [x] ⚡ Groq-powered fast inference
- [x] ☁️ Streamlit Cloud deployment
- [ ] 🧠 Chat history & memory
- [ ] 🎤 Voice input support
- [ ] 👁️ Upgrade to LLaVA / Gemini Vision
- [ ] 📊 Multi-image comparison
- [ ] 🌍 Multilingual support

---

## 👩‍💻 Author

<div align="center">

**Shalini Saurav**

*AI Engineer · Data Scientist · Builder*

Building intelligent systems that understand the world — one model at a time.

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/YOUR_USERNAME)

</div>

---

<div align="center">

### ⭐ If this helped you, star the repo — it keeps the motivation alive!

[![Try Live Demo](https://img.shields.io/badge/🚀_Live_Demo-multimodalagent.streamlit.app-a855f7?style=for-the-badge)](https://multimodalagent-gxum3ml6xovzb5vdaeucr9.streamlit.app)

<br/>

*"Building intelligent systems that understand the world like humans."*

</div>
