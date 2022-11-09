from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.conf import settings
from django.core.management import call_command
updated_on = timezone.now()

class Command(BaseCommand):
    help = "configure app custom command"

    def handle(self, *args, **options):
        print("***** Running Migrations *****")
        call_command('makemigrations')
        call_command('migrate')
        print("***** Running Test cases *****")
        #call_command('test',  'digital_twin_configure_app')
        call_command('runserver',  settings.RUNSERVER_IP+":"+settings.RUNSERVER_PORT)