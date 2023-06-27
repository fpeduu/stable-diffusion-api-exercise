# Exercício - Utilizando a Stable Diffusion API para gerar imagens a partir de linguagem natural

## Objetivo: Aprender a consumir a Stable Diffusion API para gerar imagens a partir de texto utilizando Python.

### Passo 1: Preparação do ambiente

Instale o Python em sua máquina, se ainda não estiver instalado.
Instale o pacote "requests" do Python, que será usado para fazer requisições HTTP.
Crie uma conta na Stable Diffusion API, se ainda não tiver uma.
Faça o login na Stable Diffusion API e acesse as "API Settings".
Clique em "View API Key" e copie a sua chave de API.

### Passo 2: Inicialização e importações

Crie um novo arquivo em um editor de texto e salve-o com a extensão ".py" (por exemplo, "main.py").
Importe as bibliotecas necessárias: os, requests e webbrowser.
Defina as variáveis URL e API_KEY com os valores corretos:
URL deve ser definida como 'https://stablediffusionapi.com/api/v3/text2img'.
API_KEY deve ser definida como a chave de API que você copiou.

Exemplo:

```python
import os
import requests
import webbrowser


API_KEY = 'sua chave de API'
URL = 'https://stablediffusionapi.com/api/v3/text2img'
```

### Passo 3: Implementação do programa

Solicite ao usuário o prompt de texto desejado e armazene-o em uma variável chamada prompt.
Crie uma variável chamada data para armazenar os argumentos da requisição HTTP
data deve ser um objeto com os seguintes campos:
prompt: valor igual à variável prompt.
key: valor igual à variável API_KEY.
width e height: valores iguais a 1024.

Exemplo:

```python
prompt = str(input("Enter your prompt: "))

data = {
'prompt': prompt,
'key': API_KEY,
'width': 1024,
'height': 1024
}
```

Faça uma requisição HTTP utilizando o método post da biblioteca requests. Passe a URL e os dados (data) como argumentos.
Abra o output da requisição no navegador padrão utilizando a biblioteca webbrowser.

Exemplo:

```python
response = requests.post(URL, data=data).json()

output = response['output']
output = output[0]

webbrowser.open(output)
```

### Passo 4: Execução do programa

Salve o arquivo e o execute.
Digite o prompt de texto quando solicitado.
O programa fará a requisição à Stable Diffusion API e abrirá a imagem resultante em seu navegador.

Exemplo de requisição:

Input: pope wearing a pikachu coat
Output:
![alt text](https://cdn.stablediffusionapi.com/generations/1e441785-742b-4e2d-8073-cecae5d6eed4-0.png)
