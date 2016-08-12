import requests


# Python Client for Optimus API
class Client:

    # constructor, takes licence key as param and endpoint as optional param
    def __init__(self, licence_key, endpoint='https://api.optimus.io'):
        self.__key = licence_key
        self.__endpoint = endpoint

    # getter for licence key
    def get_licence_key(self):
        return self.__key

    # setter for licence key
    def set_licence_key(self, key):
        self.__key = key

    # getter for endpoint
    def get_endpoint(self):
        return self.__endpoint

    # setter for endpoint
    def set_endpoint(self, endpoint):
        self.__endpoint = endpoint

    '''
        image - string path to file
        option - api option, optional param
        returns bytes object
        raises ConnectionError, FileNotFoundError
    '''
    def optimize(self, image, option='optimize'):
        with open(image, 'rb') as data:
            headers = {
                'user-agent': 'Optimus-API',
                'accept': 'image/*',
            }
            endpoint = '{}/{}?{}'.format(self.__endpoint, self.__key, option)
            result = requests.post(endpoint, headers=headers, data=data)
            return result.content
