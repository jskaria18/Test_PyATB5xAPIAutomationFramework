import allure
import pytest
import json

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import put_request
from src.helpers.common_verification import verify_http_status_code
from src.helpers.payload_manager import payload_update_booking
from src.utils.utils import Utils


class TestE2ETC_06(object):
    @allure.title("TC_06 Update a booking ID without token")
    @allure.description("This TC verifies the behaviour when booking details are updated without a token")
    def test_update_wo_token(self,create_token,create_and_get_booking_id):
        token = " "
        booking_id = create_and_get_booking_id

        update_url = APIConstants().url_put_patch_delete(booking_id)
        update_headers = Utils().common_headers_put_delete_patch_cookie(token)
        update_payload = payload_update_booking()

        update_response = put_request(
            url=update_url,
            headers=update_headers,
            payload=update_payload,
            auth=None,
            in_json=False
        )
        print("Response received: " ,update_response.status_code,"",update_response.text)
        verify_http_status_code(update_response, 403)
