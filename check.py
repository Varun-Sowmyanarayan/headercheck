import requests

URL="http://127.0.0.1:5002"

IMPORTANT_HEADERS=[
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

def main():
    try:
        response=requests.get(URL, timeout=5)
    except requests.exceptions.RequestException:
        print("Could not reach the site at " + URL)
        return
    print("Headercheck report for"+ URL)
    print("-" * 40)

    passed=0
    for header in IMPORTANT_HEADERS:
        if header in response.headers:
            print("PASS   " + header)
            passed+=1
        else:
            print("MISSING  " + header)
    print("-" * 40)
    print("Score: " + str(passed) + "/" + str(len(IMPORTANT_HEADERS)))

main()
