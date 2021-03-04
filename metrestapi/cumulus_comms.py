import time
import requests
import json
from pprint import pprint

# FIXME : add retries, authentication etc in the future
# returning 200 even if return data is not good - this should be 500 ?
# call ANY REST API - must be generic
def call_rest_api(endpoint, query):
    """
    Call REST API endpoint

    :param endpoint:e.g. 'http://127.0.0.1:9500/wind_deg_to_wind_rose'
    :param query: e.g. query = {'wind_deg': wind_deg}
    :return:
    """
    try:
        print('call_rest_api() : endpoint=' + endpoint)
        if query is not None:
            pprint(query.__str__())
        response = requests.get(endpoint, params=query)

        if response.status_code != 200:
            return 500, None

        response_dict = json.loads(response.content.decode('utf-8'))

        return response.status_code, response_dict

    except Exception as e:
        print('call_rest_api() : Error=' + e.__str__())
        return 500, None


def wait_until_cumulus_data_ok(cumulusmx_endpoint):
    """
    Loop until CumulusMX is returning valid data
    :param cumulusmx_endpoint:
    :return:
    """

    try:
        while True:
            print('Loop until CumulusMX returns valid data...')
            time.sleep(5 * 60)
            cumulus_weather_info = check_cumulus_data_stopped(cumulusmx_endpoint)
            if cumulus_weather_info is not None:
                print('CumulusMX is now returning valid data')
                return

    except Exception as e:
        print(e.__str__())


def check_cumulus_data_stopped(cumulus_endpoint):
    """

    """

    status_code, response_dict = call_rest_api(cumulus_endpoint, None)

    # Aercus to CumulusMX serial connection down ? - all data now invalid
    if status_code == 200 and response_dict['DataStopped'] :
        return None

    if status_code == 200:
        return response_dict
    else:
        return None
