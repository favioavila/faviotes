import requests
import simplejson as json
from endpoints import *
from assertpy import assert_that

json_template = ''' 

{
    ""email": "sydney@fife"

}
'''

data = json.loads(json_template)
response = requests.post(ENDPOINT_REGISTER_USERS, data=data)

print (response)
print (response.content)
assert_that(response.status_code).is_equal_(400)