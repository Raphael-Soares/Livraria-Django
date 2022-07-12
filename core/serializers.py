from rest_framework.serializers import ModelSerializer

from core.models import Categoria
from core.models import Livro

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"