import allure
import pytest
import json

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import delete_request, put_request
from src.helpers.common_verification import verify_http_status_code, verify_delete_response
from src.helpers.payload_manager import payload_update_booking
from src.utils.utils import Utils


class TestE2E_TC05(object):
    @allure.title("TC05_Update a deleted booking")
    @allure.description("This TC verifies the behavior when user tries to update a booking that has been deleted")

    def test_update_deleted_booking(self,create_token,create_and_get_booking_id):
        token=create_token
        booking_id=create_and_get_booking_id

        delete_url = APIConstants().url_put_patch_delete(booking_id)
        delete_headers= Utils().common_headers_put_delete_patch_cookie(token)

        delete_response = delete_request(
            url=delete_url,
            headers=delete_headers,
            auth=None,
            in_json=False
        )
        verify_http_status_code(delete_response, 201)
        verify_delete_response(delete_response.text)
        print("Status code after deletion ", delete_response.status_code,"",delete_response.text)

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
        verify_http_status_code(update_response, 405)
        print("Status code while trying to update deleted booking ID: ", update_response.status_code,"", update_response.text)


