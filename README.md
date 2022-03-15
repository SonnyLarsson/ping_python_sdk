
# Ping Payments Python SDK


Use this Python library to manage Ping Payments resources regarding payments.

## Table of contents

* [Requirements](#requirements)

* [Installation](#installation)

* [Payments API](#PaymentsAPI)


## Requirements


The SDK supports the following versions of Python:

- Python 3

## Installation

Install the latest SDK using pip:

```

pip install pingSDK

```

## Payments API

### [Payments API]

* [Merchant]

* [Payment Orders]

* [Payment]

### Usage
  
First time using Payments API? Here’s how to get started:
  
#### Get a tenant ID

To use the Payments API to manage the resources you need to get a tenant ID. A tenant ID is provided to you by Ping Payments.

When you call the Payments API, you call it using a tenant ID. A tenant ID has specific permissions to resources.
**Important** Make sure you store and access the tenant ID securely.

To use the Paymnets API, you import the PaymentsAPI class, instantiate a PaymentsAPI object, and initialize it with the appropriate tenant ID and environment. Here’s how:

1. Import the PaymentsApi class from the Ping Python SDK module so you can call the Payments API:

```python

from ping.payments_api import PaymentsApi

```
2. Instantiate a PaymentsApi object and initialize it with the teanat ID and the environment that you want to use.

To access sandbox resources, initialize the PaymentsApi with environment set to sandbox:

```python

payments_api = PaymentsApi(
		tenant_id = '55555555-5555-5555-5555-555555555555',
		environment = 'sandbox'
)

```
To access production resources, initialize the PaymentsApi with environment set to production:

```python

payments_api = PaymentsApi(
		tenant_id = '55555555-5555-5555-5555-555555555555',
		environment = 'production'
)

```
#### Get an Instance of an API object and call its methods

The API is implemented as a class. With the PaymentsApi object you work with an API by calling it's methods.

**Work with the API by calling the methods on the API object.** For example, you would call get_merchants to get a list of all merchant for the tenant:

```python

result = payments_api.merchant.get_merchants()

```
See the SDK documentation for the list of methods for the API class.

#### Handle the response

API calls return an ApiResponse object that contains properties that describe both the request (headers and request) and the response (status_code, reason_phrase, text, errors, body, and cursor). Here’s how to handle the response:

**Check whether the response succeeded or failed.** ApiResponse has two helper methods that enable you to easily determine the success or failure of a call:

```python

if result.is_success():
# Display the response as text
print({result.text})
# Call the error method to see if the call failed
elif result.is_error():
print(f"Errors: {result.errors}")

```

[//]: #  "Link anchor definitions"

[Payments API]: doc/api_resources/payments_api.md

[Merchant]: doc/api_resources/payments_api/merchant.md

[Payment Orders]: doc/api_resources/payments_api/payment_order.md 

[Payment]: doc/api_resources/payments_api/payment.md 