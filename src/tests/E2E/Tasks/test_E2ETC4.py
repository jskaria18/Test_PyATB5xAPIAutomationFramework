import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import delete_request, get_request
from src.helpers.common_verification import verify_http_status_code, verify_delete_response
from src.utils.utils import Utils


class TestE2ETC_04(object):
    @allure.title("TC_03 Get a Booking -> Delete it -> Verify")
    @allure.description("Get a specific booking from list of booking IDs, delete that booking and verify that the booking id is not available anymore")

    def test_get_specific_booking_delete_verify_booking(self,get_all_booking_ids,create_token):
        booking_id=get_all_booking_ids
        token=create_token
        delete_url = APIConstants().url_put_patch_delete(booking_id)
        headers_del = Utils().common_headers_put_delete_patch_cookie(token)

        response_del = delete_request(
            url=delete_url,
            headers=headers_del,
            auth=None,
            in_json=False
        )

        verify_http_status_code(response_del, 201)
        verify_delete_response(response_del.text)
        print("Status code description after deletion ", response_del.text)

        print("!--Verifying if the booking id is actually deleted---!")

        get_url = APIConstants().url_put_patch_delete(booking_id)
        headers_get = Utils().common_headers_json()
        response_get = get_request(
            url=get_url,
            headers=headers_get,
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_get, 404)
        print("Booking ID", booking_id, "is", response_get.text)