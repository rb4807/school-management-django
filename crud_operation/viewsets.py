from rest_framework import viewsets
from . import models
from . import serializers

class MemberViewsets(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer