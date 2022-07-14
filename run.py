""" 확장플로그램

# Basic Extenstions
1. VSCode-icons
1. Open in browser
1. indent-rainbow

# Install Extensions for Python
1. Python
1. AREPL for python
1. Kite autoComplete AI
1. autoDocstring - Python Docstring Generator
1. Python Test Explorer for Visual Studio Code


Returns:
    _type_: _description_
"""
import json


user = json.loads('{"id":100, "name":"홍길동"}')

print(f'username is {user["name"]}')



def userInfo(u):
    """_summary_

    Args:
        u (User): User Json Object

    Returns:
        String: User Information
    """
    
    
    id = u["id"]
    name = u["name"]
    return f'ID is {id}, name is {name}'

print(f'user Infomation: {userInfo(user)}')



