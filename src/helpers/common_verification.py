# this will contain all the types of Common Verification

# HTTP status code
# Headers
# Data verification
# JSON Schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed to get status code"

def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed to match the key"

#This is actually the booking id
def verify_json_key_not_null(key):
    assert key != 0 , "Failed! Key is null"

#This is actually the booking id
def verify_json_key_gr_than_zero(key):
    assert key > 0, "Key is not greater than zero"