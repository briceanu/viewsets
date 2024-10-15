from rest_framework import serializers
from .models import BlogModel



class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BlogModel
        

class UpdateBlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["content"]
        model = BlogModel
        