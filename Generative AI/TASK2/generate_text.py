import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load Fine-Tuned Model & Tokenizer
model_path = "./gpt2_finetuned"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Generate Text
def generate_text(prompt, max_length=100, temperature=0.7, top_k=50):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=max_length, temperature=temperature, top_k=top_k)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# User Input
prompt = input("Enter a prompt: ")
generated_text = generate_text(prompt)
print("\nGenerated Text:\n", generated_text)
