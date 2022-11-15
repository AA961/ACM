from .serializers import VideoSerializer
from .serializers import CategorySerializer, BlogSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Videos, Category, Blog
from django.db.models import Q


class lastBlog(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()[0:1]
        serilizer = BlogSerializer(blogs, many=True)

        return Response(serilizer.data)


class latestBlogs(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serilizer = BlogSerializer(blogs, many=True)

        return Response(serilizer.data)


class latestVideo(APIView):
    def get(self, request, format=None):
        videos = Videos.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


class videoDetail(APIView):
    def get_object(self, category_slug, videos_slug):
        try:
            return Videos.objects.filter(category__slug=category_slug).get(slug=videos_slug)
        except Videos.DoesNotExist:
            raise Http404

    def get(self, request,  category_slug, videos_slug, format=None):
        video = self.get_object(category_slug, videos_slug)
        serializer = VideoSerializer(video)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Videos.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug,)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        videos = Videos.objects.filter(Q(title__icontains=query) | Q(
            description__icontains=query))

        seralizer = VideoSerializer(videos, many=True)
        return Response(seralizer.data)

    else:
        return Response({"videos": []})

# https://themeforest.net/item/valkivid-streamer-and-youtuber-psd-template/32496915
