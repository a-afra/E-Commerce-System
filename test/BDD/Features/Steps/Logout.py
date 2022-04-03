from behave import *
import requests


@given("I am Logged in with '{username}' and '{password}' credentials")
def step_impl(context, username, password):
    url = f'http://127.0.0.1:8000/login/'

    response = requests.post(url, json={
        "username": username,
        "password": password
    })
    context.token = response.json()['token']

    assert response.status_code == 200


@when("I send Logout request")
def step_impl(context):
    url = f'http://127.0.0.1:8000/logout/'

    context.response = requests.get(url, headers={
        'Authorization': f'Token {context.token}'
    })


@then("I receive feedback that I am Logged out")
def step_impl(context):
    assert context.response.status_code == 200
    assert 'logged out.' in context.response.text


@step("I cannot visit my account page anymore")
def step_impl(context):
    url = 'http://127.0.0.1:8000/customer-info'

    response = requests.get(url, headers={
        'Authorization': f'Token {context.token}'
    })

    # 401 is for unauthorized access
    assert response.status_code == 401
