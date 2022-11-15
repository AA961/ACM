from django.urls import path, include

from videos import views


urlpatterns = [
    path('latest-videos/', views.latestVideo.as_view()),
    path('videos/<slug:category_slug>/<slug:videos_slug>/',
         views.videoDetail.as_view()),
    path('videos/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path("video/search/", views.search),
    path("blogs/", views.latestBlogs.as_view()),
    path("latest-blogs/", views.lastBlog.as_view()),

]
