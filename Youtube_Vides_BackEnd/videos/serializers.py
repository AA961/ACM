from .serializers import *
from rest_framework import serializers

from .models import Category, Videos, Blog


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
            "date",
            "video_url"
        )


    

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog

        fields = (
            "id",
            "title",
            "content",
            "get_absolute_url",
            "date",
            "Image",
        )


class CategorySerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "videos",
        )
