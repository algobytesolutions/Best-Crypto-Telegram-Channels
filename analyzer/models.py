from django.db import models

class CodeSnippet(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    analysis_result = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"CodeSnippet {self.id} ({self.language})"
