import requests


# response = requests.post('http://127.0.0.1:5000/articles/',
#                          json={'title': 'Название 1',
#                                'description': 'Описание 1'})

# response = requests.patch('http://127.0.0.1:5000/articles/5',
#                           json={'description': 'Новое описание 1'})

response = requests.get('http://127.0.0.1:5000/articles/5')

# response = requests.delete('http://127.0.0.1:5000/articles/5')

print(response.status_code)
print(response.json())