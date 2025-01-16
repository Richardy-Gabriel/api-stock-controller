from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from stock import models, serializers


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def product_list_create(request):
    """
    List and Create Products
    """
    if request.method == 'POST':
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    products = models.ProductModel.objects.all()
    serializer = serializers.ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = models.ProductModel.objects.get(pk=pk)
    except models.ProductModel.DoesNotExist:
        return Response({
            "error": "The product is not registered"
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = serializers.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = serializers.ProductSerializer(product)
    return Response(serializer.data)
