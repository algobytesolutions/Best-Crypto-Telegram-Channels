from django.test import TestCase
from .models import CodeSnippet
from .views import analyze_code_security

class CodeSnippetTests(TestCase):

    def test_syntax_error(self):
        code = "print('Hello World"
        result = analyze_code_security(code)
        self.assertEqual(result, 'Code contains syntax errors.')

    def test_secure_code(self):
        code = "print('Hello World')"
        result = analyze_code_security(code)
        self.assertEqual(result, 'Code is secure within its context.')

    def test_dangerous_function(self):
        code = "exec('print(\"Hello World\")')"
        result = analyze_code_security(code)
        self.assertEqual(result, 'Code contains dangerous functions.')

    def test_sql_injection(self):
        code = "cursor.execute('SELECT * FROM users WHERE id = ' + user_id)"
        result = analyze_code_security(code)
        self.assertEqual(result, 'Code contains potential SQL injection risks.')
