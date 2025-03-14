import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset

# Load dataset (Ensure the dataset is correctly formatted)
dataset = load_dataset("financial_phrasebank", "sentences_allagree", split="train", trust_remote_code=True)

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert", num_labels=3)

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define class labels
label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}

# Function to get response
def get_response(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class = torch.argmax(logits, dim=1).item()
    return label_map[predicted_class]

# Example Usage
if __name__ == "__main__":
    test_text = "The stock market is performing exceptionally well today."
    print(f"Sentiment: {get_response(test_text)}")
