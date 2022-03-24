import uuid
import unittest
from ping.payments_api import PaymentsApi
from test_helper import testHelper

class TestPaymentOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")
        cls.split_tree_id = "4f3a07d4-ef83-4040-bcc4-0a6e6bfab6ab"
        cls.test_helper = testHelper

    def setUp(self):
        self.payment_order_id = "bd3e750f-2213-45c5-9d02-0dbeb2178675"

# Get Payment Orders Tests
    # get payment orders correclty (status code 200)
    def test_get_payment_orders_200(self):
        response_date = self.payments_api.paymentOrder.get_payment_orders("2019-10-12", "2020-10-12")
        response = self.payments_api.paymentOrder.get_payment_orders()

        # tests with start-end date
        self.test_helper.run_tests(self, response_date)

        # tests without date
        self.test_helper.run_tests(self, response)

    # get payment orders with impossible dates (status code 422)
    def test_get_payment_orders_422(self):
        response_date = self.payments_api.paymentOrder.get_payment_orders("2019-90-12", "2020-10-40")
        self.test_helper.run_tests(self, response_date, 422)

# Create Payemnt Order Tests
    # creates a payment order correctly (status code 200)
    def test_create_payment_order_200(self):
        response = self.payments_api.paymentOrder.create_payment_order(self.split_tree_id)
        self.test_helper.run_tests(self, response)

    # creates a payment orders with incorrect id format (status code 422)
    def test_create_payment_order_422(self):
        response = self.payments_api.paymentOrder.create_payment_order(0)
        self.test_helper.run_tests(self, response, 422)

# Get Payment Order Tests
    # gets a payment order correctly (status code 200)
    def test_get_payment_order_200(self):
        response = self.payments_api.paymentOrder.get_payment_order(self.payment_order_id)
        self.test_helper.run_tests(self, response)
    
    # get a payment order with incorrect id format (status code 422)
    def test_get_payment_order_422(self):
        response = self.payments_api.paymentOrder.get_payment_order(0)
        self.test_helper.run_tests(self, response, 422)
    
    # get a payment order with a non-existing id (status code 404)
    def test_get_payment_order_404(self):
        response = self.payments_api.paymentOrder.get_payment_order(uuid.uuid4())
        self.test_helper.run_tests(self, response, 404)

# Update Payment Order Tests
    # updates a payment order correctly (status code 204)
    def test_update_payment_order_204(self):
        '''
        response = self.payments_api.paymentOrder.update_payment_order(
            self.payment_order_id,
            self.split_tree_id
        )
        self.test_helper.run_tests(self, response, 204)
        '''

    # updates a payment order with incorrect id format (status code 422)
    def test_update_payment_order_422(self):
        '''
        response = self.payments_api.paymentOrder.update_payment_order(
            0,
            self.split_tree_id
        )
        self.test_helper.run_tests(self, response, 422)
        '''

    # updates a payment order with a non-existing id (status code 404)
    def test_update_payment_order_404(self):
        '''
        response = self.payments_api.paymentOrder.update_payment_order(
            uuid.uuid4(),
            self.split_tree_id
        )
        self.test_helper.run_tests(self, response, 404)
        '''

# Close Payment Order Tests
    # closes a payment order correctly (status code 204)
    def test_close_payment_order_204(self):
        response = self.payments_api.paymentOrder.close_payment_order(self.payment_order_id)
        self.test_helper.run_tests(self, response, 204)

    # closes a payment order with an incorrect id format (status code 422)
    def test_close_payment_order_422(self):
        response = self.payments_api.paymentOrder.close_payment_order(0)
        self.test_helper.run_tests(self, response, 422)

    # closes a payment order with a non-existing id (status code 404)
    def test_close_payment_order_404(self):
        response = self.payments_api.paymentOrder.close_payment_order(uuid.uuid4())
        self.test_helper.run_tests(self, response, 404)

# Settle Payment Order Tests
    # settles a payment correctly (status code 204)
    def test_settle_payment_order_204(self):
        response = self.payments_api.paymentOrder.settle_payment_order(self.payment_order_id)
        self.test_helper.run_tests(self, response, 204)
    # settles a payment with an incorrect id format (status code 422)
    def test_settle_payment_order_422(self):
        response = self.payments_api.paymentOrder.settle_payment_order(0)
        self.test_helper.run_tests(self, response, 422)

    # settles a payment with a non-existing id (status code 404)
    def test_settle_payment_order_404(self):
        response = self.payments_api.paymentOrder.settle_payment_order(uuid.uuid4())
        self.test_helper.run_tests(self, response, 404)

# Split Payemnt Order Tests
    # splits a payment order correctly (status code 200)
    def test_split_payment_order_204(self):
        response = self.payments_api.paymentOrder.split_payment_order(self.payment_order_id)
        self.test_helper.run_tests(self, response, 204)

    # splits a payment order with an incorrect id format (status code 422)
    def test_split_payment_order_422(self):
        response = self.payments_api.paymentOrder.split_payment_order(0)
        self.test_helper.run_tests(self, response, 422)

    # splits a payment order with a non-existing id (status code 404)
    def test_split_payment_order_404(self):
        response = self.payments_api.paymentOrder.split_payment_order(uuid.uuid4())
        self.test_helper.run_tests(self, response, 404)


if __name__ == '__main__':
    unittest.main()
