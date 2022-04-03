from rest_framework import serializers

from student_app.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'amount_due', 'dob')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
