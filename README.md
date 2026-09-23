Website Security Checker

A beginner-friendly Python tool that checks a website's HTTPS connection and analyzes the presence of common HTTP security headers.

Features
Checks HTTPS connectivity
Displays the HTTP status code
Counts redirects
Checks for common security headers:
Strict-Transport-Security
Content-Security-Policy
X-Content-Type-Options
X-Frame-Options
Calculates a basic security-header score
Assigns a rating based on the percentage of detected headers
Technologies Used
Python
Requests
HTTP security headers
Linux / Ubuntu
Installation

Clone the repository:

git clone <repository-url>
cd security-checker

Install the required package:

pip install -r requirements.txt
Usage

Run:

python3 security_checker.py

Enter a website when prompted:

Enter a website: example.com

The program then displays a security report.

Disclaimer

This tool is intended for educational purposes and basic security-header analysis. Only scan websites that you own or have permission to test.

Future Improvements
Check additional security headers
Add SSL/TLS certificate information
Improve URL validation
Add command-line arguments
Export reports to a file
