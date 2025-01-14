import pytest
import allure
# import requests

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import put_request
from src.helpers.api_request_wrapper import delete_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_update_booking
from src.utils.utils import *


class TestE2E1(object):

    @allure.title("Create Booking --> Create Token --> Update the booking using token")
    @allure.description("Verify that user is able to Create Booking, followed by creating a Token which would be used to update the created booking")
    def test_update_booking_using_token(self, create_token,create_and_get_booking_id):

        print(create_token,create_and_get_booking_id)
        token=create_token
        bookingid=create_and_get_booking_id

        update_url = APIConstants().url_put_patch_delete(bookingid)
        print(update_url)
        headers=Utils().common_headers_put_delete_patch_cookie(token)
        print(headers)
        payload=payload_update_booking()

        response=put_request(
                url=update_url,
                headers=headers,
                payload=payload,
                auth=None,
                in_json=False
        )
        verify_http_status_code(response,expected_data=200)
        firstname=response.json()["firstname"]
        print("Firstname: ", firstname)
        verify_response_key(firstname,"Amit")

@allure.title("Create Booking --> Create Token --> Update the booking using token")
@allure.description("Verify that user is able to Create Booking, followed by creating a Token which would be used to update the created booking")

def test_delete_booking(create_token,create_and_get_booking_id):
                print(create_token, create_and_get_booking_id)
                token_test = create_token
                booking_id = create_and_get_booking_id

                delete_url=APIConstants().url_put_patch_delete(booking_id)
                print(delete_url)
                delete_headers=Utils().common_headers_put_delete_patch_cookie(token_test)
                print(delete_headers)

                response=delete_request(
                    url=delete_url,
                    headers=delete_headers,
                    auth=None,
                    in_json=False
                )
                print(response.content)
                verify_http_status_code(response,201)
                verify_delete_response(response.text)
