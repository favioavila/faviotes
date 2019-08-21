import requests
import simplejson as json
from endpoints import *
from assertpy import assert_that

json_template = ''' 

{
    "email": "peter@klaven"
}
'''

data = json.loads(json_template)
response = requests.post(ENDPOINT_LOGIN_USERS, data=data)

print (response)
print (response.content)
assert_that(response.status_code).is_equal_(400)
