from rest_framework import viewsets
from .serializers import ApiSerializer
from .models import ApiModel

# Create your views here.
class ApiViewSet(viewsets.ModelViewSet):
    queryset = ApiModel.objects.all()
    serializer_class = ApiSerializer
