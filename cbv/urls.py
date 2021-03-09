"""cbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
# from student.views import ListingStudent, StudentDetail
# from student.views import StudentList, DetailStudent
from student.views import StudentList2, DetailStudent2, StudentViewSet
from rest_framework.routers import DefaultRouter
from nsApp.author.views import ListAuthor, DetailAuthor
from nsApp.books.views import ListBook, DetailBook
from nsApp.customer.views import ListCustomer, DetailCustomer
from nsApp.order.views import ListOrder, DetailOrder


router = DefaultRouter()
router.register('student', StudentViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    # # path('listing_student/', ListingStudent.as_view()),
    # # path('student/<int:pk>/', StudentDetail.as_view()),
    # path('listing_student/', StudentList2.as_view()),
    # path('student/<int:pk>/', DetailStudent2.as_view())
    path('', include(router.urls)),
    # path('author/', ListAuthor.as_view()),
    # path('author/<int:pk>/', DetailAuthor.as_view()),
    # path('book/', ListBook.as_view()),
    # path('book/<int:pk>/', DetailBook.as_view()),
    path('customer/', ListCustomer.as_view()),
    path('customer/<int:pk>/', DetailCustomer.as_view()),
    path('order/', ListOrder.as_view()),
    path('order/<int:pk>/', DetailOrder.as_view()),
]
