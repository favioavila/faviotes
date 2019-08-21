import requests
from endpoints import *

from assertpy import assert_that

response = requests.get(ENDPOINT_UNKNOWN + "/23")

print (response)
print (response.content)

assert_that(404).is_equal_to(response.status_code)