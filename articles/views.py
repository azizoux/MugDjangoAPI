from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True, methods=['POST'])
    def save_file(self, request, pk=None):
        if 'file' in request.data:
            file = request.FILES['file']
            file_name = default_storage.save(file.name, file)
            return JsonResponse(file_name, safe=False)
        else:
            response = {'message': 'You need to provide file'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)