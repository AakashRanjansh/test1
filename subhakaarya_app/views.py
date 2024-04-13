from .models import Service, Plan, Event, VendorService, Vendorlist
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ServiceSerializer, PlanSerializer, EventSerializer, VendorServiceSerializer, VendorlistSerializer
from django.conf import settings
from django.core.mail import send_mail


class ServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_superuser:
            return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            service = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorServiceView(APIView):
    def get(self, request):
        services = VendorService.objects.all()
        serializer = VendorServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user:
            return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = VendorServiceSerializer(data=request.data)
        if serializer.is_valid():
            service = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanView(APIView):
    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_superuser:
            return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            plan = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VendorlistView(APIView):
    def get(self, request):
        vendorlist = Vendorlist.objects.all()
        serializer = VendorlistSerializer(vendorlist, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     if not request.user.is_superuser:
    #         return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    #     serializer = PlanSerializer(data=request.data)
    #     if serializer.is_valid():
    #         plan = serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = VendorlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will create a new Vendorlist instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EventView(APIView):
    def get(self, request):
        if not request.user.is_superuser:
            return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)

        events = Event.objects.all().order_by('-id')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['number_of_people'] = data.get('numberOfPeople')
        data['event_date'] = data.get('eventDate')
        data['event_location'] = data.get('eventLocation')

        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            event = serializer.save()
            for service in data.get('services'):
                event.services.add(Service.objects.get(id=service))

            email_admins(data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def email_admins(data):
    subject = f"New booking by {data.get('owner')} at {data.get('event_location')}"
    message = f"""
                Name: {data.get('owner')}
                Email: {data.get('email')}
                Phone: {data.get('phone')}
                Total people: {data.get('number_of_people')}
                Date: {data.get('event_date')}
                Location: {data.get('event_location')}
            """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = settings.ADMINS_EMAIL
    send_mail(subject, message, email_from, recipient_list)
