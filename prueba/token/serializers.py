from rest_framework import serializers
from token.models import Token
#escribiendo sobre las tablas
class TokenModelSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class."""

        model = Token
        fields = (
            'pk',
            'valor',
            'fechaRegistro'
        )
class TokenSerializer(serializers.Serializer):
    idToken=serializers.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    valor=serializers.CharField(max_length=6)
    fechaRegistro = serializers.DateTimeField(auto_now_add=True, blank=True)

    def create(self, data):

        exp = Token.objects.create(**data)
        return exp