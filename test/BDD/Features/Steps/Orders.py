from behave import *
import requests


@when("I navigate to my orders")
def step_impl(context):
    url = 'http://127.0.0.1:8000/customer-info'

    context.response = requests.get(url, headers={
        'Authorization': f'Token {context.token}'
    })

    assert context.response.status_code == 200


@then("I see a list of my orders")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json()[0]['orders'] is not None


@step("I can open an order to see the order details")
def step_impl(context):
    url = context.response.json()[0]['orders'][0]['url']

    response = requests.get(url, headers={
        'Authorization': f'Token {context.token}'
    })

    assert response.status_code == 200
