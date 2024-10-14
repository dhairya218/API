# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Webtoon
from .serializers import WebtoonSerializer

# GET /webtoons: Fetch all webtoons
@api_view(['GET'])
def webtoon_list(request):
    webtoons = Webtoon.objects.all()
    serializer = WebtoonSerializer(webtoons, many=True)
    return Response(serializer.data)

# POST /webtoons: Add a new webtoon (requires authentication)
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure JWT authentication for POST requests
def webtoon_create(request):
    serializer = WebtoonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET /webtoons/<id>: Fetch a specific webtoon by its ID
@api_view(['GET'])
def webtoon_detail(request, id):
    webtoon = get_object_or_404(Webtoon, id=id)
    serializer = WebtoonSerializer(webtoon)
    return Response(serializer.data)

# DELETE /webtoons/<id>: Delete a webtoon by its ID (requires authentication)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # Ensure JWT authentication for DELETE requests
def webtoon_delete(request, id):
    webtoon = get_object_or_404(Webtoon, id=id)
    webtoon.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
