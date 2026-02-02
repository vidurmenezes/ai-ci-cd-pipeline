import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read CI test results
with open("result.log", "r") as f:
    test_results = f.read()

# Build prompt for AI
prompt = f"""
Here are the test results from CI:

{test_results}

Summarize any failures and provide short suggestions for fixing them.
"""

# Call OpenAI chat completion API
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful CI assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150
)

# Extract and print AI summary
summary = response.choices[0].message.content
print("AI SUMMARY:")
print(summary)
