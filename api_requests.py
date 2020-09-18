import requests
import json
from api_key import my_api_key


# Put in your api key!!!
API_KEY = my_api_key
MAIN_URL = 'https://api.um.warszawa.pl/api/action/'


def make_request(end_link, params):
    """ Function that makes a request to the api and returns the data queried if all parameters are valid
            Note: make sure to fill in your api key for the global variable API_KEY above

    Args:
        end_link (string): sub-link to be added to the main link (https://api.um.warszawa.pl/api/action), 
                            for example 'dbstore_get' or 'busestrams_get' (don't include '/')
        params (dict): dictionary with all parameters and their values for the api request

    Returns:
        requests.models.Response

    Example call:
        make_request('busestrams_get', dict(type=1))

    """
    url = MAIN_URL + end_link
    response = requests.get(url, params=params)
    return response

def json_print(response):
    """ Checks whether request was successful and if so, 'pretty' prints json object contained in the response object
    Args:
        response (requests.models.Response): response object returned from api request
    """
    if response:
        print('Response OK')
        print(json.dumps(response.json(), sort_keys=True, indent=4))
        if(response.json()["result"] == "false"):
            print('REQUEST FAILED - check api_key and/or other parameters')
    else:
        print('Response Failed')
        print(f'Status code: {response.status_code}')



def busestrams_get(other_params=None):
    """ Prints the json object obtained by the api request to 'https://api.um.warszawa.pl/api/action/busestrams_get'
        (Goal is to write similar functions for other 'sub-links' with their corresponding resource-ids
        Benefit: only takes in the other parameters, no need to look up sub-link/resource_id every time or include api key)
    Args:
        other_params(dict): for specifying the other parameters to be included in the api request
    """
    end_link = 'busestrams_get'
    resource_id = 'f2e5503e-927d-4ad3-9500-4ab9e55deb59'
    if other_params is None:
        other_params = {}
    other_params['resource_id'] = resource_id
    other_params['apikey'] = API_KEY
    json_print(make_request(end_link, other_params))



def main():

    # Example for which a function has been written:
    busestrams_get(dict(type=1))

    # Examples for which a functions has not been written yet:
        # note: the below request returns '[]' --> maybe the stop 'nazwaprzystanku' isn't active anymore?
    """ 
    end_link = 'dbtimetable_get'
    params = dict(id='b27f4c17-5c50-4a5b-89dd-236b282bc499', name='nazwaprzystanku', apikey=API_KEY)
    json_print(make_request(end_link, params))

    end_link = 'dbstore_get'
    params = dict(id='ab75c33d-3a26-4342-b36a-6e5fef0a3ac3', apikey=API_KEY)
    json_print(make_request(end_link, params))
    """



if __name__ == "__main__":
    main()