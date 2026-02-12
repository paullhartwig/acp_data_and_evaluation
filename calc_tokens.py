import json

# Replace with your file path
file_path = './data/user_study/prompt_logs_tester_07.json'

with open(file_path, 'r') as f:
    data = json.load(f)

input_tokens = 0
output_tokens = 0

for prompt in data.get('prompts', []):
    for log in prompt.get('logs', []):
        usage = log.get('metadata', {}).get('usage', {})
        input_tokens += usage.get('prompt_tokens', 0)
        output_tokens += usage.get('completion_tokens', 0)

print(f"Total input tokens: {input_tokens}")
print(f"Total output tokens: {output_tokens}")