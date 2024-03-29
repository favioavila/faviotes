from settings import *

# List all endpoints here

PARTIAL_USERS = "/api/users"
PARTIAL_REGISTER_USERS = "/api/register"
PARTIAL_UNKNOWN = "/api/unknown"
PARTIAL_LOGIN_USERS = "/api/login"

# Complete endpoints

ENDPOINT_USERS = WEB_SERVER + PARTIAL_USERS

ENDPOINT_UNKNOWN = WEB_SERVER + PARTIAL_UNKNOWN

ENDPOINT_REGISTER_USERS = WEB_SERVER + PARTIAL_REGISTER_USERS

ENDPOINT_LOGIN_USERS = WEB_SERVER + PARTIAL_LOGIN_USERS
