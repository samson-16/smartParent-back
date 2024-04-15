from .models import User , Student , Parent , Teacher
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='id')
    username = serializers.EmailField(source='email')

    class Meta:
        model = User
        fields = ['user_id','username', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'], 
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            password=validated_data['password'] 
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
class ParentListSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user.id', read_only=True)
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')
    children = StudentSerializer(many=True) 

    class Meta:
        model = Parent
        fields = ['id', 'user_id', 'first_name', 'last_name', 'email', 'phone_number', 'children']

class TeacherSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')
    user_id = serializers.ReadOnlyField(source='user.id') 

    class Meta:
        model = Teacher
        fields = ['id', 'user_id', 'first_name', 'last_name', 'email', 'phone_number']