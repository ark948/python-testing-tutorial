from unittest.mock import Mock

mock = Mock()

# mock the api function
# assign a return value to a function called api
mock.api.return_value = {
    "id": 1,
    "message": 'hello'
}

print(mock.api)

print(mock.api())