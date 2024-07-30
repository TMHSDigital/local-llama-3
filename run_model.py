from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("path/to/models", use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained("path/to/models", use_auth_token=True)

# Tokenize input
inputs = tokenizer("Hello, how are you?", return_tensors="pt")

# Generate output
with torch.no_grad():
    outputs = model.generate(inputs["input_ids"], max_length=50)

# Decode and print the output
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
