#!/usr/bin/env python3
"""Test the exam submission endpoint with fallback grading"""

import httpx
import json

# Test data
test_data = {
    "student_name": "John Doe",
    "student_email": "john@example.com",
    "q1": "Smith",
    "q2": "555-1234",
    "q3": "Toothache",
    "q4": "Tuesday",
    "q5": "10:00",
    "r1": "B",
    "r2": "B",
    "r3": "B",
    "r4": "B",
    "r5": "B",
    "r6": "accessible",
    "r7": "weight",
    "r8": "injuries",
    "r9": "stress",
    "r10": "natural",
    "writing_answer": "Walking is an excellent form of exercise that offers many health benefits. It improves cardiovascular health and helps maintain a healthy weight. Furthermore, it is accessible to people of all ages and fitness levels, making it an ideal activity for anyone.",
    "speaking_link": "https://example.com/audio.mp3"
}

print("Submitting exam with fallback grading...")
print("=" * 60)

try:
    print(f"Sending data: {json.dumps(test_data, indent=2)[:200]}...\n")
    response = httpx.post(
        "http://127.0.0.1:8000/submit_exam",
        data=test_data,
        timeout=60.0
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print("\n✓ SUCCESS!")
        print(f"\nMessage: {result.get('message')}\n")
        
        results = result.get('results', {})
        print("Writing Feedback:")
        print("-" * 40)
        print(results.get('writing_feedback'))
        
        print("\n\nSpeaking Feedback:")
        print("-" * 40)
        print(results.get('speaking_feedback'))
        
        print("\n\nObjective Results:")
        print("-" * 40)
        obj = results.get('objective_results', {})
        print(f"Score: {obj.get('score')}/{obj.get('total')}")
        
    else:
        print(f"\n✗ Error: {response.text}")
        
except Exception as e:
    print(f"✗ Exception: {e}")

print("\n" + "=" * 60)
print("Test complete!")
