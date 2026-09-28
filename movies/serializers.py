from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'genre',
            'release_year',
            'status',
            'status_display',
            'rating',
            'created_at',
            'owner',
        ]
        read_only_fields = ['id', 'created_at', 'owner']

    def validate_release_year(self, value):
        if value < 1888 or value > 2100:
            raise serializers.ValidationError("Buraxılış ili düzgün deyil")
        return value

    def validate_rating(self, value):
        if value is not None and not (1 <= value <= 10):
            raise serializers.ValidationError("Qiymətləndirmə 1-dən 10-a qədər olmalıdır")
        return value
