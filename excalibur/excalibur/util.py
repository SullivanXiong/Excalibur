import json

def save_to_dataset(prompt, response):
    data = {'input': prompt, 'output': response}
    with open('../llm_data.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
