#!/usr/bin/env python3
"""Quick test to verify HF token and model access"""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
if HF_TOKEN:
    HF_TOKEN = HF_TOKEN.strip().strip('"').strip("'")
else:
    print("ERROR: HF_TOKEN not found in environment!")
    exit(1)

print(f"HF_TOKEN: {HF_TOKEN[:20]}...")

# List of models to try
models_to_try = [
    "gpt2",
    "distilgpt2",
    "tiiuae/falcon-7b-instruct",
    "meta-llama/Llama-2-7b-chat-hf",
    "mistralai/Mistral-7B-Instruct-v0.1",
]

test_prompt = "Hello, how are you?"

for model in models_to_try:
    print(f"\n{'='*60}")
    print(f"Testing model: {model}")
    print(f"{'='*60}")
    
    url = f"https://router.huggingface.co/hf-inference/models/{model}"
    headers = {"Authorization": f"Bearer {HF_TOKEN}", "Content-Type": "application/json"}
    payload = {"inputs": test_prompt, "parameters": {"max_new_tokens": 50}}
    
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=30.0)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print(f"✓ SUCCESS! Response: {response.json()}")
        else:
            try:
                err = response.json()
                print(f"✗ Error: {err}")
            except:
                print(f"✗ Error: {response.text}")
    except Exception as e:
        print(f"✗ Exception: {e}")

print(f"\n{'='*60}")
print("Test complete!")
