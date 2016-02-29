from rest_client import rest_api as rest, rest_errors

resp = rest.get_data()
if resp.status_code != 200:
    raise rest_errors.ApiError(resp.status_code, "Unable to get data.")
print(resp.json())
