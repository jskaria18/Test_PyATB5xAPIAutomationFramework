
import pytest
import requests

from src.constants.api_constants import *
from src.helpers.api_request_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *

@pytest.fixture(scope="session")
def create_token():
    token_url = APIConstants().url_create_token()
    token_headers=Utils().common_headers_json()
    token_payload=payload_create_token()

    response=post_request(
        url=token_url,
        headers=token_headers,
        auth=None,
        payload=token_payload,
        in_json=False
    )
    verify_http_status_code(response_data=response,expected_data=200)
    verify_json_key_not_None(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def create_and_get_booking_id():
    url=APIConstants().url_create_booking()
    headers=Utils().common_headers_json()
    payload=payload_create_booking()

    response=post_request(
        url=url,
        headers=headers,
        auth=None,
        payload=payload,
        in_json=False
    )

    verify_http_status_code(response_data=response,expected_data=200)
    # bookingid=response.json()["bookingid"]
    # verify_json_key_not_None(bookingid)
    verify_json_key_not_None(response.json()["bookingid"])
    print("Booking ID ", response.json()["bookingid"], "is created")
    return response.json()["bookingid"]
    # return bookingid

@pytest.fixture(scope="session")
def get_all_booking_ids():
        url=APIConstants().get_all_booking_ids()
        headers_for_get_all = Utils().common_headers_json()

        response_for_get_all = requests.get(url=url,headers = headers_for_get_all  )

        get_all_response_jsonpayload = response_for_get_all.json()
        #print("GETALL IDs response ", get_all_response_jsonpayload)
        print("Taking one specific Booking ID from list of Booking IDs")
        if get_all_response_jsonpayload:
          bookin_ids = get_all_response_jsonpayload[0]["bookingid"]
          print("Got this booking ID from the list of booking IDs -->", bookin_ids)
          return bookin_ids
        else:
            print("No booking IDs found")
            return  None



