import torch
from transformers import pipeline


# ==========================================
# AI RESEARCH ASSISTANT
# ==========================================

# Select GPU if available, otherwise CPU
device = 0 if torch.cuda.is_available() else -1

print("Loading AI models...")
print("Device:", "GPU" if device == 0 else "CPU")


# ==========================================
# RESEARCH TEXT
# ==========================================

research_text = """
Artificial Intelligence (AI) is transforming scientific research by automating complex data analysis.
Machine learning algorithms detect patterns in large datasets faster than many people can.
In healthcare, AI models assist doctors in diagnosing diseases early by analyzing medical images.
In climate science, AI helps forecast weather patterns and model long-term climate change impacts.
However, AI adoption requires careful consideration of ethical factors, data privacy, and algorithmic bias.
Ensuring transparency and fairness in automated decision-making systems remains a critical goal for researchers.
"""


# ==========================================
# TEXT SUMMARIZATION
# ==========================================

print("\nLoading summarization model...")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    device=device
)


summary_result = summarizer(
    research_text,
    max_length=60,
    min_length=25,
    do_sample=False,
    truncation=True
)

summary = summary_result[0]["summary_text"]


print("\n================================")
print("RESEARCH SUMMARY")
print("================================")
print(summary)


# ==========================================
# QUESTION ANSWERING
# ==========================================

print("\nLoading question-answering model...")

qa_model = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    device=device
)


# ==========================================
# SINGLE QUESTION
# ==========================================

question = "What ethical concerns are mentioned about AI?"

answer = qa_model(
    question=question,
    context=research_text
)


print("\n================================")
print("QUESTION ANSWERING")
print("================================")
print("QUESTION:", question)
print("ANSWER:", answer["answer"])
print("CONFIDENCE:", round(answer["score"], 4))


# ==========================================
# MULTIPLE QUESTIONS
# ==========================================

questions = [
    "How does AI help healthcare?",
    "How does AI help climate science?",
    "What is a critical goal for AI researchers?"
]


print("\n================================")
print("MULTIPLE QUESTIONS")
print("================================")


for question in questions:

    answer = qa_model(
        question=question,
        context=research_text
    )

    print("\nQuestion:", question)
    print("Answer:", answer["answer"])
    print("Confidence:", round(answer["score"], 4))