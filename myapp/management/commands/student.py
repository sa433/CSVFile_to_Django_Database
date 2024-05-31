import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import Student
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Import student from csv file'

    def handle(self, *args, **kwargs):

        data_dir = os.path.join(settings.BASE_DIR, 'data')

        csv_file_path = os.path.join(data_dir, 'stud.csv')

        try:
            df = pd.read_csv(csv_file_path)

            df['name'] = df['name'].fillna(value='Unknown')
            df['age'] = df['age'].ffill()
            df['city'] = df['city'].fillna(value='Unknown')


        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('CSV file not found'))
            return

        for _,row in df.iterrows():
            Student.objects.create(
                name=row['name'],
                age=row['age'],
                city=row['city']
            )

        self.stdout.write(self.style.SUCCESS('File Upload successfully'))
