from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer, VendorSerializer
from verify_email.email_handler import send_verification_email
from django.contrib.auth import login
from .models import Vendor
from .forms import VendorForm


class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response(None, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user).data,
                "message": "User Created Successfully.",
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorView(APIView):
    serializer_class = VendorSerializer

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request, *args,  **kwargs):
        serializer = self.serializer_class(data=request.data)
        form = VendorForm(request.POST)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "vendor": UserSerializer(user).data,
                "message": "User Created Successfully",
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
