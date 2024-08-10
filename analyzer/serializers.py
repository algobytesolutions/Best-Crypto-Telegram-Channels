from rest_framework import serializers
from .models import CodeSnippet

class CodeSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnippet
        fields = ['id', 'code', 'language', 'created_at', 'analysis_result']
        extra_kwargs = {
            'language': {'required': False}
        }
