from __future__ import annotations

from django.core.management import call_command
from django.core.management.base import BaseCommand


class ETLCommand(BaseCommand):
    help = 'Run ETL pipeline.'

    def handle(self, *args, **kwargs):

        call_command('extract')
        call_command('transform')
        call_command('load')

        self.stdout.write(self.style.SUCCESS(
            'ETL pipeline executed successfully.'))


Command = ETLCommand
