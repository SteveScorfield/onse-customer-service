from builtins import NotImplementedError

from behave import when, then


@when(u'the customer "{cust_id}" changes their name to "{cust_name}"')
def change_customer_name(context, cust_id, cust_name):
    (first_name, surname) = cust_name.split(' ', 2)
    response = context.web_client.put(
        f'/customers/{cust_id}',
        json={'firstName': first_name, 'surname': surname})

    assert response.status_code == 200, \
        f'Status code = {response.status_code}; expected 200'


@then(u'customer "{cust_id}" should be "{cust_name}"')
def assert_name_change(context, cust_id, cust_name):
    response = context.web_client.get(f'/customers/{cust_id}')

    assert response.status_code == 200, \
        f'Status code = {response.status_code}; expected 200'
    customer = response.get_json()
    returned_name = f"{customer['firstName']} {customer['surname']}"
    assert  returned_name == cust_name, \
        f'Expected customer name {cust_name} but {returned_name} instead'
