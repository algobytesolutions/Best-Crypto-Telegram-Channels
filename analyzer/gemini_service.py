import requests
from django.conf import settings

def analyze_code_snippet(code):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": f"""
Analyze the following code for security vulnerabilities and best practices. Provide the output in bullet points for each section. but do not include dashes or asterisks for the points, just normally write the text. Keep the content concise and to the point, without any additional narrative. Do not keep the headings in your response as they're already handled on our frontend, just write it's content in points. don't include headings in your response. which are (Vulnerabilities, Suggested Fixes, Best Practices, Overall Security Score) just write it's content which i ask for:

1. Vulnerabilities: List vulnerabilities as [Severity] : Vulnerability Name - Short description.
2. Suggested Fixes: Provide very short and actionable fixes in points.
3. Best Practices: Mention best practices in short bullet points.
4. Overall Security Score: Provide a numerical score on a scale of 0 to 100.

Code:
{code}
                    """}
                ]
            }
        ]
    }
    params = {
        'key': settings.GEMINI_API_KEY
    }
    response = requests.post(settings.GEMINI_API_URL, headers=headers, json=data, params=params)
    response.raise_for_status()
    return response.json()
