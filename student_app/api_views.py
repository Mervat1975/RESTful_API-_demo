from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from student_app.serializers import StudentSerializer
from student_app.models import Student


class StudentsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description')
    pagination_class = StudentsPagination


class StudentCreate(CreateAPIView):
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        try:
            amount_due = request.data.get('amount_due')
            if amount_due is not None and float(amount_due) <= 0.0:
                raise ValidationError({'amount_due': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'amount_due': 'A valid number is required'})
        return super().create(request, *args, **kwargs)


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        student_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('student_data_{}'.format(student_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            student = response.data
            cache.set('student_data_{}'.format(student['id']), {
                'first_name': student['first_name'],
                'last_name': student['last_name'],
                'due_amount': student['due_amount'],
                'dob': student['dob'],
            })
        return response
