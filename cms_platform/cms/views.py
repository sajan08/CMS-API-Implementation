from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser, Content
from .serializers import UserSerializer, ContentSerializer
from .permissions import IsAdminOrAuthor
from rest_framework.decorators import action

# User Registration
class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login (JWT Token)
class LoginUserView(APIView):
    def post(self, request):
        email = self.request.data.get('email')
        print("email ===========", email)
        password = self.request.data.get('password')
        print("password ===========", password)
        user = authenticate(email=email, password=password)
        print("user==========", user)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'access': str(refresh.access_token), 'refresh': str(refresh)}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# Content Management
class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    permission_classes = [IsAdminOrAuthor]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Content.objects.all()
        return Content.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        print(f"Authenticated user: {self.request.user}")
        serializer.save(author=self.request.user)

    # Search content
    @action(detail=False, methods=['GET'])
    def search(self, request):
        query = request.query_params.get('q', '')
        contents = Content.objects.filter(title__icontains=query) | \
                   Content.objects.filter(body__icontains=query) | \
                   Content.objects.filter(summary__icontains=query) | \
                   Content.objects.filter(categories__icontains=query)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)
