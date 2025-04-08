from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import user
from .serializers import apiserializer



# Create your views here.
@api_view(['GET'])
def get_user(req):
    user1=user.objects.all()
    serlz=apiserializer(user1,many=True)
    return Response(serlz.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user(req):
    serlz=apiserializer(data=req.data)
    if serlz.is_valid():
        serlz.save()
        return Response(serlz.data,status=status.HTTP_202_ACCEPTED)
    return Response(serlz.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updation_user(req,pk):
    try:
        user1=user.objects.get(pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    serlz=apiserializer(user1,data=req.data)
    if serlz.is_valid():
        serlz.save()
        return Response(serlz.data,status=status.HTTP_202_ACCEPTED)
    
@api_view(['DELETE'])
def delete_user(pk):
    try:
        user=object.all.get(pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    user.delete()
    return Response(status=status.HTTP_100_CONTINUE)


    

     

