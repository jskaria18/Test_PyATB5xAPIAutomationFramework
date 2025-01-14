import allure
import pytest
import json

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import put_request
from src.helpers.common_verification import verify_http_status_code
from src.helpers.payload_manager import payload_update_booking, payload_update_patch_booking
from src.utils.utils import Utils


class TestE2ETC_06(object):
    @allure.title("TC_06 Update a booking ID using Invalid PUT request")
    @allure.description("This TC verifies the behaviour when invalid payload is provided for PUT request")
    def test_invalid_put(self,create_token,create_and_get_booking_id):
        token = create_token
        booking_id = create_and_get_booking_id

        update_url = APIConstants().url_put_patch_delete(booking_id)
        update_headers = Utils().common_headers_put_delete_patch_cookie(token)
        update_payload = payload_update_patch_booking() # Invalid payload supplied here

        update_response = put_request(
            url=update_url,
            headers=update_headers,
            payload=update_payload,
            auth=None,
            in_json=False
        )
        print("Response received: " ,update_response.status_code,"",update_response.text)
        verify_http_status_code(update_response, 400)
