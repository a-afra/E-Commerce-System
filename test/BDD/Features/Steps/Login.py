from behave import *
import requests


@given("I am not Logged in")
def step_impl(context):
    pass


@step("I am on the Login page")
def step_impl(context):
    context.password = 123
    pass


@when("I enter my {username} and {password}")
def step_impl(context, username, password):
    context.username = username
    context.password = password


@when("I send request to '{endpoint}'")
def step_impl(context, endpoint):
    url = f'http://127.0.0.1:8000{endpoint}'

    context.response = requests.post(url, json={
        "username": context.username,
        "password": context.password
    })


@then("I am Logged in.")
def step_impl(context):
    assert context.response.status_code == 200


@then("I should see '{message}'.")
def step_impl(context, message):
    assert context.response.json()[0] == message
