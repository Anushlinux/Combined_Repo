"""
URL configuration for courses_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import CourseListCreateView, CourseDetailView, CourseInstanceListCreateView, CourseInstanceDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListCreateView.as_view(), name='course-instance-list-create'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', CourseInstanceDetailView.as_view(), name='course-instance-detail'),
]
