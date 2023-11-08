from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

import time

from psycopg2 import OperationalError as PsycopError

class Command(BaseCommand):
    def handle(self,*args,**options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up= True
            except(OperationalError,PsycopError):
                self.stdout.write("Database unavailable, retrying in 1 sec.")
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS("Database Available"))