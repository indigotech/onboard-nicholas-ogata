import requests

url = 'http://127.0.0.1:8000'

def test_get_all_users():
    response = requests.get(url+'/users')

    assert response.status_code == 200

    assert response.headers['Content-Type'] == 'application/json'

    data = response.json()

    assert isinstance(data, list)
    assert 'id' in data[0]
    assert 'username' in data[0]
    assert 'age' in data[0]
    assert 'email' in data[0]
    assert 'is_active' in data[0]

def test_create_user():
    new_user = {'username': 'UserTest', 'age': 40, 'email': 'usertest@email.com'}
    response = requests.post(url+'/users', json=new_user)

    assert response.status_code == 201

    assert response.headers['Content-Type'] == 'application/json'

    data = response.json()

    assert 'id' in data
    assert data['username'] == 'UserTest'
    assert data['age'] == 40
    assert data['email'] == 'usertest@email.com'
