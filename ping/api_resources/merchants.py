import requests

class Merchants():

    def __init__(self, tenant_id):
        self.base_url = 'http://sandbox.pingpayments.com/payments'
        self.tenant_id = tenant_id

    def get_merchants(self):
        """Does a GET request to /api/v1/merchants. 
        
        Lists merchants associated with a tenant. The merchant details
        include email, id, name, organization number and phone number. 

        Args:
            None arguments.  

        Returns:
            Response: An object with the response value as well as other
            useful information such as status codes and headers.  

        Raises:
            APIException: When an error occurs while fetching the data from
            the remote API. This exception includes the HTTP Response
            code, an error message, and the HTTP body that was received in
            the request.
        """

        #Prepare URL 
        _path = '/api/v1/merchants'
        _url = self.base_url + _path

        #Prepare header 
        _header = {
            "Accept": "application/json",
            "tenant_id": self.tenant_id
        }

        #Prepare and execute response
        _response = requests.get(_url, headers=_header)
        return _response

    def create_new_merchants(self, object):
        """Does a POST request to /api/v1/merchants. 
        
        Creates a new merchants for a tenant. 
        You must provide a object with the following values:
        - "name"
        - "organization_number"

        Args:
            Body: An object containing the fields to
            POST for the request.  

        Returns:
            Response: An object with the response value as well as other
            useful information such as status codes and headers.  

        Raises:
            APIException: When an error occurs while fetching the data from
            the remote API. This exception includes the HTTP Response
            code, an error message, and the HTTP body that was received in
            the request.
        """

        #Prepare URL
        _path = '/api/v1/merchants'
        _url = self.base_url + _path

        #Prepare header 
        _header = {
            "Accept": "application/json",
            "tenant_id": self.tenant_id
        }
        
        #Prepare and execute response 
        _response = requests.post(_url, headers=_header,json=object)
        return _response

    def get_specific_merchant(self, merchant_id):
        """Does a GET request to /api/v1/merchants/{merchant_id}. 
        
        Returns details for a single merchant. The details include email, id,
        name, organization name, organization number, phone_number and status.

        Args:
            merchant_id (string). The ID of the of the merchant to retrive. 

        Returns:
            Response: An object with the response value as well as other
            useful information such as status codes and headers.  

        Raises:
            APIException: When an error occurs while fetching the data from
            the remote API. This exception includes the HTTP Response
            code, an error message, and the HTTP body that was received in
            the request.
        """

        #Prepare URL
        _path = f'/api/v1/merchants/{merchant_id}'
        _url = self.base_url + _path

        #Prepare header 
        _header = {
            "Accept": "application/json",
            "tenant_id": self.tenant_id
        }

        #Prepare and execute response 
        _response = requests.get(_url, headers=_header)
        return _response
