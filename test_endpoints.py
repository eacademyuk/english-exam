#!/usr/bin/env python3
"""Test different HF API endpoints"""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
if HF_TOKEN:
    HF_TOKEN = HF_TOKEN.strip().strip('"').strip("'")
else:
    print("ERROR: HF_TOKEN not found!")
    exit(1)

print(f"HF_TOKEN: {HF_TOKEN[:20]}...")

test_prompt = "Hello"
model = "gpt2"

endpoints = [
    f"https://api-inference.huggingface.co/models/{model}",
    f"https://router.huggingface.co/hf-inference/models/{model}",
    f"https://huggingface.co/api/models/{model}",
]

for url in endpoints:
    print(f"\n{'='*60}")
    print(f"Testing: {url}")
    print(f"{'='*60}")
    
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": test_prompt}
    
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=15.0)
        print(f"Status: {response.status_code}")
        
        if response.status_code in [200, 503]:  # 503 means model is loading
            try:
                print(f"Response: {response.json()}")
            except:
                print(f"Response: {response.text}")
        else:
            try:
                print(f"Error: {response.json()}")
            except:
                print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")
