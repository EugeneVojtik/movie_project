from django.core.management import BaseCommand

from movies.models import Reviews


class Command(BaseCommand):
    def handle(self, *args, **options):
        queryset = Reviews.objects.all()
        for query in queryset:
            query.delete()
