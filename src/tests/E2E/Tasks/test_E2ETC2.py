
import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import delete_request, get_request
from src.helpers.common_verification import verify_http_status_code, verify_delete_response
from src.utils.utils import Utils


class TestE2ETC_02(object):
    @allure.title("TC_02Create Booking -> Delete It -> Verify")
    @allure.description("Created a booking, delete that booking and verify that the booking_id is actually deleted")

    def test_delete_booking_and_confirm_deletion(self,create_token,create_and_get_booking_id):
        booking_id=create_and_get_booking_id
        token=create_token
        delete_url=APIConstants().url_put_patch_delete(booking_id)
        headers_del=Utils().common_headers_put_delete_patch_cookie(token)

        response_del=delete_request(
            url=delete_url,
            headers=headers_del,
            auth=None,
            in_json=False
        )

        verify_http_status_code(response_del,201)
        verify_delete_response(response_del.text)
        print("Status code description after deletion ",response_del.text)

        print("!--Verifying if the booking id is actually deleted---!")

        get_url=APIConstants().url_put_patch_delete(booking_id)
        headers_get=Utils().common_headers_json()
        response_get=get_request(
            url=get_url,
            headers=headers_get,
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_get,404)
        print("Booking ID",booking_id,"is",response_get.text)



