def get_customer(customer_id, customer_repository):
    return customer_repository.fetch_by_id(customer_id)


def create_customer(customer, customer_repository):
    customer_repository.store(customer)


def update_customer(customer_id, customer_repository, firstname, surname):
    customer = customer_repository.fetch_by_id(customer_id)
    customer.first_name = firstname
    customer.surname = surname
    customer_repository.store(customer)
