from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
  return HttpResponse('WORKING')

@api_view(['GET'])
def getAlldata(request):
  lista = Product.objects.all()
  serializer  = ProductSerializer(lista, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create(request):
  if request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message": "Data saved successfully!"})
    else:
      return Response(serializer.error)




# def create(request):
#   print(request.POST)
#   if request.method == 'POST':
#     form = EmpleadoForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('index')
#   else:
#     # INITIALIZER EmpleadoForm,THEN FORM.AS_P CAN WORK  
#     form = EmpleadoForm()
#   data = {'msg': 'registro guardado2', 'form': form}
#   return render(request, 'client/create.html', data)