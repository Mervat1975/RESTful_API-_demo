from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import student_app.views
import student_app.api_views

urlpatterns = [
    path('api/v1/students/',
         student_app.api_views.StudentList.as_view(), name='api-view'),
    path('api/v1/students/new',
         student_app.api_views.StudentCreate.as_view(), name='api-new'),
    path('api/v1/students/<int:id>/',
         student_app.api_views.StudentRetrieveUpdateDestroy.as_view(), name='api-update'
         ),

    path('admin/', admin.site.urls),
    path('students/<int:id>/', student_app.views.show, name='show-student'),
    path('', student_app.views.index, name='list-students'),
]
