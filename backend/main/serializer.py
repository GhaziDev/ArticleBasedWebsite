from rest_framework import serializers,fields
from main import models
from drf_extra_fields.fields import Base64ImageField
from PIL import Image
from io import BytesIO
import base64




class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = 'id','title','title_img','description','tag','user','date'
        model = models.Article


class TagSerializer(serializers.ModelSerializer):
    tag_articles = ArticleSerializer(many=True,read_only=True)
    
    class Meta:
        fields = ('name','tag_articles')
        lookup_field = 'name'
        extra_kwargs = {
            'url':{'lookup_field':'name'}
        }
        model = models.Tag

    
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = models.Comment

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Signup


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=False,allow_null=True,allow_blank=True)


class SearchSerializer(serializers.Serializer):
    search = serializers.CharField(required=False)


class CheckUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)


class OnEditSerializer(serializers.Serializer):
    description = serializers.CharField()    