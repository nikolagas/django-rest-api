from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class ApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            ''
        ]

        return Response({'message': 'Hi!', 'apiview': apiview})
