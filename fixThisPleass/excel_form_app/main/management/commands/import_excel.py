from django.core.management.base import BaseCommand
import pandas as pd
from main.models import Person

class Command(BaseCommand):
    help = "Import Excel data into PostgreSQL"

    def handle(self, *args, **kwargs):
        # Load the Excel file
        df = pd.read_excel('main/excel_data/test3.xlsx')

        # Loop through rows and save to PostgreSQL
       # print("Excel columns:", df.columns) 
        #return
        for _, row in df.iterrows():
            Person.objects.create(
            ari8mosEisagoghs=row['ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'],
            hmeromhnia_eis=row['ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ'],
            syggrafeas=row['ΣΥΓΓΡΑΦΕΑΣ'],
            koha=row['ΣΥΓΓΡΑΦΕΑΣ KOHA'],
            titlos=row['ΤΙΤΛΟΣ'],
            ekdoths=row['ΕΚΔΟΤΗΣ'],
            ekdosh=row['ΕΚΔΟΣΗ'],
            etosEkdoshs=row['ΕΤΟΣ ΕΚΔΟΣΗΣ'],
            toposEkdoshs=row['ΤΟΠΟΣ  ΕΚΔΟΣΗΣ'],
            sxhma=row['ΣΧΗΜΑ'],
            selides=row['ΣΕΛΙΔΕΣ'],
            tomos=row['ΤΟΜΟΣ'],
            troposPromPar=row['ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ'],
            ISBN=row['ISBN'],
            sthlh1=row['Στήλη1'],
            sthlh2=row['Στήλη2'])
            

        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
