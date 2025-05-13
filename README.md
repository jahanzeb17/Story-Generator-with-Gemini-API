# ✨ AI-Powered Story Generator

An interactive web application that generates compelling multi-chapter stories based on custom character inputs and plot premises. Built using **Streamlit**, **LangChain**, and **Google's Gemini API**, this tool leverages the power of generative AI to craft original stories tailored to your preferences.

---

## 🚀 Live Demo

> Link: [https://story-generator-by-jahanzeb17.streamlit.app/].

---

## 📌 Key Highlights

- ✅ **Dynamic Story Generation** — Create stories with a custom character, location, personality, and genre.
- 📖 **Structured Format** — Each story includes a prologue, chapter outlines, 5–10 full chapters, and an epilogue.
- 🧠 **Creativity Toggle** — Choose between low or high creativity levels for different tones and styles.
- 📂 **Downloadable Output** — Instantly download the generated story as a `.txt` file.
- 🔐 **Secure API Access** — Uses environment variables to keep API keys safe.

---

## 🛠️ Tech Stack

| Tool/Library         | Purpose                                 |
|----------------------|------------------------------------------|
| Streamlit            | Frontend for interactive UI              |
| LangChain            | Prompt orchestration & API calls         |
| Google Gemini API    | Generative AI model for story creation   |
| python-dotenv        | Securely load API keys from `.env`       |

---

## 🧪 How It Works

1. User fills in story details (name, character type, etc.)
2. Selects the story length, premise(s), and creativity level
3. App constructs a tailored prompt and sends it to Gemini via LangChain
4. Gemini responds with a complete, chapter-based story
5. User views and optionally downloads the story

---

## 📦 Installation Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-story-generator.git
cd ai-story-generator
