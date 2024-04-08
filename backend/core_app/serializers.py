from .models import User , Student , Parent , Teacher
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(source='email')  # Use email as username

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],  # Use email as username
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            password=validated_data['password']  # Include password
        )
        return user
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')
    children = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'children']

class TeacherSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']