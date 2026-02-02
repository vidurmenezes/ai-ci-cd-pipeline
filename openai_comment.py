import os
import openai
from github import Github

# Load API keys
openai.api_key = os.environ['OPENAI_API_KEY']
github_token = os.environ['GITHUB_TOKEN']
repo_name = os.environ['GITHUB_REPOSITORY']
pr_number = os.environ['GITHUB_REF'].split('/')[-2]

# Read test results
with open('result.log', 'r') as f:
    test_output = f.read()

# Prepare prompt for OpenAI
prompt = f"Summarize the following test results and suggest next steps:\n\n{test_output}"

# Call OpenAI API
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100:
)

summary = response.choices[0].text.strip()

# Post comment on PR
g = Github(github_token)
repo = g.get_repo(repo_name)
pr = repo.get_pull(int(pr_number))
pr.create_issue_comment(f"🤖 AI Test Summary:\n\n{summary}")
