import requests


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options"
]


def check_security_headers(response):
    score = 0

    for header in SECURITY_HEADERS:
        if response.headers.get(header) is None:
            print("[-]", header + ": Missing")
        else:
            print("[+]", header + ": Present")
            score += 1

    return score


def get_rating(percentage):
    if percentage == 100:
        return "Excellent"
    elif percentage >= 75:
        return "Good"
    elif percentage >= 50:
        return "Fair"
    else:
        return "Poor"


def main():
    print("=== Website Security Checker ===")

    target = input("Enter a website: ")
    url = "https://" + target

    try:
        response = requests.get(url, timeout=5)

        print()
        print("=== Website Security Report ===")
        print("Target:", target)

        print()
        print("--- Connection ---")
        print("HTTPS: PASS")
        print("Status Code:", response.status_code)

        if response.history:
            print("Redirects:", len(response.history))
        else:
            print("Redirects: None")

        print()
        print("--- Security Headers ---")

        score = check_security_headers(response)
        total = len(SECURITY_HEADERS)

        percentage = (score / total) * 100
        rating = get_rating(percentage)

        print()
        print("--- Security Score ---")
        print("Security Score:", score, "/", total)
        print("Security Percentage:", percentage, "%")
        print("Rating:", rating)

    except requests.RequestException as error:
        print()
        print("[-] HTTPS: FAILED")
        print("Error:", error)


if __name__ == "__main__":
    main()
