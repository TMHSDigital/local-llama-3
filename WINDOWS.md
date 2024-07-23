# Setting Up LLaMA 3 on Windows

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.9-blue)
![LLaMA 3](https://img.shields.io/badge/LLaMA-3-orange)

## Introduction

This guide provides detailed instructions for setting up and running the LLaMA 3 model locally on your Windows machine. Follow the steps below to get started.

## Prerequisites

Ensure you have the following installed on your Windows machine:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Step-by-Step Instructions

### 1. Install Python

Download and install Python from the official website:

[![Install Python](https://img.shields.io/badge/Install%20Python-FFD343?logo=python&style=for-the-badge)](https://www.python.org/downloads/)

Make sure to check the box to add Python to your PATH during the installation.

### 2. Install Git

Download and install Git from the official website:

[![Install Git](https://img.shields.io/badge/Install%20Git-F05032?logo=git&style=for-the-badge)](https://git-scm.com/downloads)

### 3. Set Up a Virtual Environment

Open Command Prompt and set up a virtual environment for your project:

```bash
python -m venv llama3_env
llama3_env\Scripts\activate
```

### 4. Install Required Packages

Install the necessary packages:

```bash
pip install torch
```

[![Install Required Packages](https://img.shields.io/badge/Install%20Packages-orange?logo=pypi&style=for-the-badge)](https://pypi.org/)

### 5. Clone the Repository

Clone the `local-llama-3` repository:

```bash
git clone https://github.com/TMHSDigital/local-llama-3.git
cd local-llama-3
```

### 6. Acquire the Model

#### Download the Model Weights

You might need to download the model weights manually from the official source if they are not available on Hugging Face.

### 7. Running the Model

Create a Python script (`run_model.py`) with the following content:

```python
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
```

### 8. Running the Script

Run the script to generate text:

```bash
python run_model.py
```

## Resources

- [Python](https://www.python.org/)
- [Git](https://git-scm.com/)

## License

This project is licensed under the MIT License.

![MIT License](https://img.shields.io/badge/license-MIT-blue)

---

## Buttons for Quick Navigation

[![Python](https://img.shields.io/badge/Install%20Python-FFD343?logo=python&style=for-the-badge)](https://www.python.org/downloads/)
[![Git](https://img.shields.io/badge/Install%20Git-F05032?logo=git&style=for-the-badge)](https://git-scm.com/downloads)
[![LLaMA 3](https://img.shields.io/badge/LLaMA-3-orange?logo=llama&style=for-the-badge)](https://ollama.com/library/dolphin-llama3:latest/blobs/ea025c107c1c)
```
