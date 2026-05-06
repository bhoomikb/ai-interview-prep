# 🤖 AI Interview Prep Assistant

A Python CLI tool powered by **Anthropic's Claude API** that generates personalized interview questions and strong sample answers — tailored to any job description and your specific background.

> Built to demonstrate real-world Claude API usage, prompt engineering, and Python development skills.

---

## 🎯 What It Does

Paste in a job description + your background and get:

- ✅ **Top 10 interview questions** specific to the role
- ✅ **Tailored sample answers** using your own experience
- ✅ **Key skills to highlight** from the job description
- ✅ **A smart question to ask the interviewer**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| Anthropic Python SDK | Claude API integration |
| Streaming API | Real-time response output |

---

## 📂 Project Structure

```
ai-interview-prep/
├── app.py            # Main CLI application
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your Anthropic API key
export ANTHROPIC_API_KEY="your-api-key-here"

# 3. Run the app
python app.py
```

You'll be prompted to paste a job description and your background, then Claude generates your full prep guide in real time.

---

## 💬 Example Output

```
🎯 AI Interview Prep Assistant
Powered by Claude (Anthropic)
============================================================

Generating your personalized interview prep guide...

============================================================
TOP 10 INTERVIEW QUESTIONS:

1. Can you walk me through your experience with manual testing?
2. How do you write effective test cases for a new feature?
3. Describe a bug you found that had significant impact...
...
============================================================
✅ Interview prep complete! Good luck! 🍀
```

---

## 💡 Key Concepts Demonstrated

- 🔑 Anthropic Claude API integration (claude-opus-4-5)
- 🌊 Streaming responses for real-time output
- 📝 Prompt engineering for structured, role-specific output
- 🐍 Clean Python CLI design

---

## 🎓 Certifications

This project was built using skills from:
- **Anthropic Claude API Certification** (Completed)
- **Anthropic AI Fluency Certification** (Completed)

---

## 👩‍💻 Author

**Bhoomi Bhavsar** — CS Graduate | Manual QA Tester | Anthropic AI Certified  
[LinkedIn](https://www.linkedin.com/in/bhoomi-bhavsar)
