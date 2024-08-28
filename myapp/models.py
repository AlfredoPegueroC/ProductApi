from django.db import models
from rest_framework import serializers
# Create your models here.
class Product(models.Model):
  Codigo = models.CharField(max_length=50, null=False)
  Descripcion = models.CharField(max_length=100, null=False)
  Precio = models.CharField(max_length=50, null=False)
  Tipo = models.CharField(max_length=50, null=False)

  def __str__(self):
    return f'  {self.Codigo} {self.Descripcion} {self.Precio} {self.Tipo}'


class ProductSerializer(serializers.Serializer):
  Codigo = serializers.CharField(max_length=50)
  Descripcion = serializers.CharField(max_length=100)
  Precio = serializers.CharField(max_length=50)
  Tipo = serializers.CharField(max_length=50)

  class Meta:
    model: Product
    field: ['__all__']


  def create(self, validated_data):
        # You can add any custom logic here
        product= Product.objects.create(
            Codigo=validated_data['Codigo'],
            Descripcion=validated_data['Descripcion'],
            Precio=validated_data['Precio'],
            Tipo=validated_data['Tipo'],
        )
        return product
