import requests

def scan(url):
    payload = "' OR '1'='1"
    vulnerable = False

    try:
        response = requests.get(url + payload)
        if "syntax" in response.text.lower():
            vulnerable = True
    except:
        pass

    return "Vulnerable" if vulnerable else "Not Vulnerable"
