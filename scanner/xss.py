import requests

def scan(url):
    payload = "<script>alert('XSS')</script>"
    vulnerable = False

    try:
        response = requests.get(url + payload)
        if payload in response.text:
            vulnerable = True
    except:
        pass

    return "Vulnerable" if vulnerable else "Not Vulnerable"
