import requests
from endpoints import *

from assertpy import assert_that

response = requests.delete(ENDPOINT_USERS + "/2")

print (response)
print (response.content)

assert_that(204).is_equal_to(response.status_code)