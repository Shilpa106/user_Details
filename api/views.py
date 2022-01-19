from django.shortcuts import render

# Create your views here.
from . models import Person
from .serializers import PersonSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PersonApiView(APIView):
    def get(self, request, *args, **kwargs):

        """
        get list of persons
        """

        userdetail = Person.objects.all()
        serializer = PersonSerializers(userdetail, many=True)

    
        data = {
                "description": "ok",
                "items": serializer.data
                }

            
        return Response(data,status=status.HTTP_200_OK)
    


    def post(self, request, *args, **kwargs):

        """
        create api for User Details
        """

        if Person.objects.filter(email=request.data.get("email")).exists():
            return Response({"description": "Email Already Taken"},status=status.HTTP_409_CONFLICT)
       
        serializer_obj = PersonSerializers(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()

            data={

                  "description": "User Created",
                  "items": serializer_obj.data
                 }
            return Response(data, status=status.HTTP_200_OK)
        return Response({"description":"Missing Required Information"}, status=status.HTTP_400_BAD_REQUEST)

    
    




class PersonView(APIView):
    def get(self, request, *args, **kwargs):

        """
        get Person by id
        """

       
        id = self.kwargs.get("pk")       
        
        if id is not None:           
            try:
                user_detail = Person.objects.get(id=id)
                serializer = PersonSerializers(user_detail)
                data = {
                    "description": "User Found",
                    "items": [serializer.data]
                }
                
                return Response(data,status=status.HTTP_200_OK)
            except Person.DoesNotExist:
                return Response({"description":"User not Found"},status=status.HTTP_404_NOT_FOUND)



    
    def put(self, request, *args, **kwargs):

        """
        update User Details
        """

        id = self.kwargs.get("pk")
        try:
            user_det = Person.objects.get(id=id)
            userserializer = PersonSerializers(user_det, data=request.data)
            if userserializer.is_valid():
                userserializer.save()
                data = {
                    "description": "ok",
                    "items": [userserializer.data]
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    

    
    def delete(self, request, *args, **kwargs):


        """
        delete User Details
        """

        id = self.kwargs.get("pk")
        try:
            userdetail = Person.objects.get(id=id)

            deleted_item={'userdetail':str(userdetail)}
            
            
            data = {
                "description": "ok",
                "items": [deleted_item]
            }

            userdetail.delete()
            return Response(data,status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response({"description": "Person does not exist with specified id"},status=status.HTTP_400_BAD_REQUEST)


