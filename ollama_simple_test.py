# import ollama

# desired_model = "llama3.1:latest"
# questionToAsk =  "how to solve differential equations?"

# response = ollama.chat(model = desired_model, messages = [{
#     'role': "user",
#     'content': questionToAsk
# },
# ])

# OllamaResponse = response['message']["content"]
# print(OllamaResponse)

import json

# Opening JSON file
f = open('car_models_3.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
print(data)