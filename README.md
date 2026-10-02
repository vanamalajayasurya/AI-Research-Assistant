# 🔬 AI Research Assistant

A lightweight Python tool that uses pretrained **Hugging Face Transformers** models to **summarize research text** and **answer questions** about it — fully offline after the first model download, with automatic GPU/CPU selection.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white)
![Transformers](https://img.shields.io/badge/🤗%20Transformers-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Text Summarization** – condenses a long passage into a short summary using DistilBART.
- **Question Answering** – extracts precise answers from the text using RoBERTa, with a confidence score.
- **Batch Questions** – ask multiple questions in one run.
- **Auto Device Detection** – uses your GPU (CUDA) if available, otherwise falls back to CPU.
- **Zero API keys** – everything runs locally.

---

## 🧠 Models Used

| Task | Model | Source |
|------|-------|--------|
| Summarization | `sshleifer/distilbart-cnn-12-6` | [Hugging Face](https://huggingface.co/sshleifer/distilbart-cnn-12-6) |
| Question Answering | `deepset/roberta-base-squad2` | [Hugging Face](https://huggingface.co/deepset/roberta-base-squad2) |

Models are downloaded automatically on first run and cached locally (~1.5 GB total).

---

## 📁 Project Structure

```
.
├── app.py              # Main script (summarization + QA)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

**2. (Recommended) Create a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

> 💡 For GPU support, install the CUDA build of PyTorch from [pytorch.org](https://pytorch.org/get-started/locally/) first.

---

## ▶️ Usage

```bash
python app.py
```

The script will:

1. Detect whether a GPU is available.
2. Load the summarization model and summarize the research text.
3. Load the question-answering model.
4. Answer a single question, then a list of questions.

### Sample Output

```
Loading AI models...
Device: CPU

================================
RESEARCH SUMMARY
================================
<generated summary of the text>

================================
QUESTION ANSWERING
================================
QUESTION: What ethical concerns are mentioned about AI?
ANSWER: ethical factors, data privacy, and algorithmic bias
CONFIDENCE: 0.xxxx

================================
MULTIPLE QUESTIONS
================================

Question: How does AI help healthcare?
Answer: diagnosing diseases early by analyzing medical images
Confidence: 0.xxxx
```

*(Exact answers and confidence scores will vary slightly by model version.)*

---

## 🛠️ Customization

**Use your own text** – replace the `research_text` variable in `app.py`:

```python
research_text = """
Paste your own article, abstract, or notes here.
"""
```

**Change the questions** – edit the `questions` list:

```python
questions = [
    "Your question here?",
    "Another question?"
]
```

**Adjust summary length** – tune `max_length` and `min_length` in the summarizer call:

```python
summary_result = summarizer(research_text, max_length=60, min_length=25, do_sample=False, truncation=True)
```

---

## 🔧 How It Works

```
Research Text ──► DistilBART ──► Summary
       │
       └──────► RoBERTa (SQuAD2) ◄── Question ──► Answer + Confidence
```

- **DistilBART** is a distilled, faster version of BART fine-tuned on CNN/DailyMail for abstractive summarization.
- **RoBERTa-base (SQuAD2)** performs *extractive* QA: it finds the answer span inside the given context and returns a confidence score. It can also recognize unanswerable questions.

---

## 🚀 Future Improvements

- [ ] Load text from PDF / TXT files
- [ ] Interactive CLI for asking custom questions
- [ ] Web interface (Streamlit or Flask)
- [ ] Support for long documents via chunking
- [ ] Export summaries and answers to a file

---

## 🐛 Troubleshooting

| Problem | Fix |
|---------|-----|
| Slow first run | Models are being downloaded; later runs use the cache. |
| `CUDA out of memory` | Set `device = -1` to force CPU. |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt`. |
| Summary is cut off or odd | Increase `max_length` or provide longer input text. |

---

## 🤝 Contributing

Contributions are welcome! Fork the repo, create a feature branch, and open a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Vanamala Jayasurya**
Computer Science (Data Science) • Hyderabad, India

- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-profile](https://linkedin.com/in/your-profile)

⭐ If you found this project useful, consider giving it a star!
