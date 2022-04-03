from behave import *
import requests


@when("I navigate to the personal information page")
def step_impl(context):
    url = 'http://127.0.0.1:8000/customer-info'

    context.response = requests.get(url,
                                    headers={'Authorization': f'Token {context.token}'})

    assert context.response.status_code == 200


@step("I update my details")
def step_impl(context):
    url = 'http://127.0.0.1:8000/customer-update/'

    context.response = requests.patch(url,
                                      headers={'Authorization': f'Token {context.token}'},
                                      json={'description': 'Account is under test.'})

    assert context.response.status_code == 200


@then("I receive feedback that '{message}'")
def step_impl(context, message):
    assert context.response.json()['message'] == message


@step("I change my street name")
def step_impl(context):
    url = 'http://127.0.0.1:8000/customer-update/'

    context.response = requests.patch(url,
                                      headers={'Authorization': f'Token {context.token}'},
                                      json={'street_name': 'street 23'})

    assert context.response.status_code == 200
