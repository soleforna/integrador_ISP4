from django.contrib.auth import authenticate
from django.utils import timezone

from rest_framework import serializers

from apps.users.models import User
from apps.payments.api.serializers import PaymentSerializer

from django.contrib.auth.hashers import check_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','is_premium', 'is_staff')


class UserPaymentSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'payments']
    

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True)
    new_password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not check_password(value, user.password):
            raise serializers.ValidationError("La contraseña antigua no es correcta.")
        return value

    def validate(self, data):
        # Puedes agregar aquí cualquier validación adicional que necesites
        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        """
        Validar el formato y si exisate el email.
        """
        # Verificar si el email existe 
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email no está registrado")
        return value

    def validate(self, data):
        """
        Autenticar, si falla es por la contraseña.
        """
        # Obtener el email del contexto
        email = data.get('email')
        # Autenticar al usuario usando el email y la contraseña
        user = authenticate(username=email, password=data.get('password'))
        if user is None: 
            # Si la autenticación falla, levantar un error asociado al campo 'password'
            raise serializers.ValidationError({"password": "Contraseña incorrecta"})
        return data


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [ 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.last_login = timezone.now()
        user.set_password(password)
        user.save()
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class isPremiumSerializer(serializers.Serializer):
    email=serializers.EmailField()
    key=serializers.CharField()
