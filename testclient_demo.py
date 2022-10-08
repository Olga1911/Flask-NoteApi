from app import app

test_client = app.test_client()

# user_data = {
#    'username': 'test-user',
#    'password': 'test-user'
# }
# response = test_client.post('/users',
#                       json=user_data,
#                       content_type='application/json')
#
# print("json = ", response.json)
# print("code = ", response.status_code)

# users_data = [
#    {'username': 'user1', 'password': '12345'},
#    {'username': 'user2', 'password': '12345'},
#    {'username': 'user3', 'password': '12345'},
# ]
# for user in users_data:
#
#     response = test_client.post('/users',
#                       json=user,
#                       content_type='application/json')
#
# print("json = ", response.json)
# print("code = ", response.status_code)

#Получаем всех ранее созданных пользователей
# response = test_client.get('/users')
# print("json = ", response.json)
# print("code = ", response.status_code)

#Получаем пользователя по id:
response = test_client.get('/users/3')
print("json = ", response.json)
print("code = ", response.status_code)

# #Удаляем пользователя по id
# response = test_client.delete('/users/3')
# print(response.data)

