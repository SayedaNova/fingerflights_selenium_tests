import time
import re
import requests

def get_latest_email_id():
    response = requests.get("http://178.128.114.165:7040/api/v1/messages")
    messages = response.json().get("messages", [])
    return messages[0]["ID"] if messages else None

def wait_for_new_otp(previous_id, timeout=30):
    url = "http://178.128.114.165:7040/api/v1/messages"
    start_time = time.time()

    while time.time() - start_time < timeout:
        response = requests.get(url)
        messages = response.json().get("messages", [])

        if messages and messages[0]["ID"] != previous_id:
            msg_id = messages[0]["ID"]
            detail = requests.get(f"http://178.128.114.165:7040/api/v1/message/{msg_id}").json()
            body = detail.get("Text", "") or detail.get("HTML", "")
            match = re.search(r"\b\d{6}\b", body)
            if match:
                return match.group(0)
        time.sleep(1)

    return None
