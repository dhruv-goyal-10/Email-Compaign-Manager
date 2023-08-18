from rest_framework import status
from core.serializers import UserSerializer, UnsubscribeUserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.exceptions import APIException


class CreateUserView(CreateAPIView):
    
    serializer_class = UserSerializer
    
    def post(self, request):
        data = super().post(request).data
        return Response(
                {
                    "success": True,
                    "message": "Resource Created Successfully",
                    "data" : data
                },
                status=status.HTTP_201_CREATED
            )
    
class UnsubscribeUserView(UpdateAPIView):
    
    serializer_class = UnsubscribeUserSerializer
    
    def get_object(self):
        user_qs = User.objects.filter(id = self.kwargs['user_id'])

        if user_qs.exists():
            return user_qs.first()
        
        raise APIException(
                        {
                            "success": False,
                            "message" : "User does not exist"
                        },
                        code = status.HTTP_400_BAD_REQUEST
                    )


    def patch(self, request, user_id):
        super().patch(request, user_id)
        return Response(
                {
                    "success": True,
                    "message": "Operation Performed Successfully",
                },
                status=status.HTTP_200_OK,
            )