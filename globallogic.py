import requests
import json
import time

# send /get request and validate response code
base_url = "https://httpbin.org"
get_response = requests.get(base_url)
assert get_response.status_code == 200
f"GET request failed with status code {get_response.status_code}"

#send /post request with json body and validate response contain relevant data
data = {"type":"new", "valid":True}
headers = {"Content-Type": "application/json"}
post_response =requests.post(base_url, data=json.dumps(data), headers=headers).json()
assert post_response["type"] is "new", "response data doesn't match"

#validate request with delayed response delay/{delay_time}
delay_time=3
start_time = time.time()
delay_response = requests.get(base_url)
response_time = time.time() - start_time
assert (response_time - delay_time) < 1, "response exceeds the allowed delay time"

#validate any negative scenario
invalid_data = {"valid":False} #invalid data
try:
    invalid_response = requests.post(base_url, data=json.dumps(invalid_data), headers=headers).json()
    assert False, "request with invalid data succeded"
except requests.exceptions.RequestException as e:
    print(e)
    
#simulate unauthorized access
header ={"Content-Type": "application/json", "Authorization": "Invalid Token"}
response = requests.get(base_url, headers=header)
assert response.status_code in 401,403
f"unauthorized request not detected: {response.status_code}"
