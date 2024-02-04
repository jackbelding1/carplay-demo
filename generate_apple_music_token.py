import jwt
import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Replace these variables with your actual details
TEAM_ID = "G87PY825HS"
KEY_ID = "N33GZF7PVS"
PATH_TO_PRIVATE_KEY = "./AuthKey_N33GZF7PVS.p8"

# Load the private key
with open(PATH_TO_PRIVATE_KEY, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Prepare the token's headers and payload
headers = {
    "alg": "ES256",
    "kid": KEY_ID
}

payload = {
    "iss": TEAM_ID,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=4380), # 6 months validity
    "iat": datetime.datetime.utcnow()
}

# Generate the JWT
token = jwt.encode(
    payload=payload,
    key=private_key,
    algorithm='ES256',
    headers=headers
)

print("Developer Token:", token)

