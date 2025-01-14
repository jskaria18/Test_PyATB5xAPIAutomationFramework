import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import patch_request, get_request
from src.helpers.common_verification import verify_http_status_code, verify_response_key, verify_json_key_not_None
from src.helpers.payload_manager import payload_update_patch_booking
from src.utils.utils import Utils


class TestE2E_03(object):
    @allure.title("TC_03 Create Booking -> Update Booking (Patch)")
    @allure.description("Create a booking, make a patch update and verify if the update has been successful")

    def test_create_patch_verify_booking(self,create_token,create_and_get_booking_id):
        booking_id=create_and_get_booking_id
        token=create_token
        patch_url=APIConstants().url_put_patch_delete(booking_id)
        patch_headers=Utils().common_headers_put_delete_patch_cookie(token)
        patch_payload=payload_update_patch_booking()

        response_patch=patch_request(
            url=patch_url,
            headers=patch_headers,
            payload=patch_payload,
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_patch,200)
        verify_json_key_not_None(response_patch.json()["totalprice"])
        totalprice=response_patch.json()["totalprice"]
        print(totalprice)

        verify_response_key(response_patch.json()["firstname"],"Amit")
        verify_response_key(response_patch.json()["lastname"],"Hazel")
        json_patch_response = response_patch.json()
        print("Json Response", json_patch_response)

        print("!--Verifying if the Name is actually updated---!")

        get_url = APIConstants().url_put_patch_delete(booking_id)
        headers_get = Utils().common_headers_json()
        response_get = get_request(
            url=get_url,
            headers=headers_get,
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_get, 200)
        json_get_response=response_get.json()
        print("Json Response", json_get_response)
