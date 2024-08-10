import logging
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CodeSnippet
from .serializers import CodeSnippetSerializer
from .gemini_service import analyze_code_snippet
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def index(request):
    return HttpResponse("Welcome to SiteFend API. Use /api/analyze/ to analyze code.")

@api_view(['POST'])
def analyze_code(request):
    logging.debug(f'Received request data: {request.data}')
    serializer = CodeSnippetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        code = serializer.data['code']
        logging.debug(f'Code: {code}')

        try:
            gemini_result = analyze_code_snippet(code)
            detailed_report = parse_gemini_response(gemini_result)
            overall_score = extract_overall_score(gemini_result)
        except Exception as e:
            gemini_result = f'Error analyzing with Gemini API: {str(e)}'
            detailed_report = None
            overall_score = "N/A"

        result = {
            'gemini_analysis': gemini_result,
            'detailed_report': detailed_report,
            'overall_score': overall_score
        }

        snippet = CodeSnippet.objects.get(id=serializer.data['id'])
        snippet.analysis_result = result
        snippet.save()
        return Response({'result': result})
    else:
        logging.debug(f'Serializer errors: {serializer.errors}')
    return Response(serializer.errors, status=400)

def parse_gemini_response(gemini_result):
    report_content = gemini_result["candidates"][0]["content"]["parts"][0]["text"]

    vulnerabilities = extract_section(report_content, "Vulnerabilities", "Suggested Fixes")
    suggested_fixes = extract_section(report_content, "Suggested Fixes", "Best Practices")
    best_practices = extract_section(report_content, "Best Practices", "Overall Security Score")

    # Extract the overall security score separately
    overall_score = extract_overall_score(report_content)

    return {
        "vulnerabilities": vulnerabilities,
        "suggested_fixes": suggested_fixes,
        "best_practices": best_practices,
        "overall_score": overall_score
    }

def extract_section(content, section_name, next_section_name):
    try:
        # Locate the start of the section
        start_idx = content.find(section_name)
        if start_idx == -1:
            return ""

        # The section ends either at the next section or the end of the text
        end_idx = content.find(next_section_name, start_idx + len(section_name))
        if end_idx == -1:
            end_idx = len(content)

        # Extract and clean up the section content
        section_content = content[start_idx:end_idx].strip()
        section_content = section_content.replace("**", "").replace(f"{section_name}:", "").strip()

        # Ensure each point starts on a new line
        section_content = section_content.replace("- ", "\n- ").strip()

        return section_content
    except Exception as e:
        return ""

import re

def extract_overall_score(gemini_result):
    try:
        # Extract the main content from the response
        score_section = gemini_result["candidates"][0]["content"]["parts"][0]["text"]

        # Print the full score_section to see its contents
        print("Score Section:", score_section)

        # Use a regular expression to find the score, accounting for asterisks
        match = re.search(r"Overall Security Score:\s*(\d+)", score_section)
        if match:
            score_value = match.group(1)
            return score_value
        else:
            return "Not provided"
    except Exception as e:
        print("Error in extract_overall_score:", str(e))
        return "Not provided"













