from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Leave
from .serializer import LeaveSerializer, UserSerializer


class LeaveList(generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def post(self, request, *args, **kwargs):
    #     start_date = self.request.data.get('start_date')
    #     end_date = self.request.data.get('end_date')
    #     leave_type = self.request.data.get('leave_type')
    #     note = self.request.data.get('note')
    #     owner = self.request.user
    #     Leave.objects.create(start_date=start_date, end_date=end_date, leave_type=leave_type, note=note, owner=owner)
    #     success_message = {'message': 'Leave submitted successfully'}
    #     return Response(success_message, status=status.HTTP_201_CREATED)


class LeaveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

