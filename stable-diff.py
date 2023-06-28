import os
import requests
import webbrowser
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY') # Sua chave de API
URL = 'https://stablediffusionapi.com/api/v3/text2img'

prompt = str(input("Enter your prompt: "))

data = {
      'prompt': prompt,
      'key': API_KEY,
      'width': 1024,
      'height': 1024
    }

response = requests.post(URL, data=data).json()

output = response['output']
output = output[0]

webbrowser.open(output)
