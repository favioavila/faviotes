import requests
from endpoints import *

from assertpy import assert_that

response = requests.get(ENDPOINT_UNKNOWN)

print (response)
print (response.content)

assert_that(200).is_equal_to(response.status_code)
