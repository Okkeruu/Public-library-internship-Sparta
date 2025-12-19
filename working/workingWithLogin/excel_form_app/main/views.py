from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pandas as pd
from .forms import UploadExcelForm, CustomUserCreationForm
from .models import Person, UploadLog
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def home(request):
    return render(request, 'home.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def clean(value):
    if pd.isna(value):
        return None
    return str(value).strip()

@login_required
def show_people(request):
    people = Person.objects.all()
    return render(request, 'main/people.html', {'people': people})

@login_required
def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)

        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            added = []
            updated = []
            skipped = []

            for _, row in df.iterrows():
                ari8mos = clean(row.get('ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'))

                if ari8mos is None:
                    skipped.append({
                        'row': index + 2,
                        'reason': 'Missing ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'
                    })
                    continue

                obj, was_created = Person.objects.update_or_create(
                    ari8mosEisagoghs=ari8mos,  # PRIMARY KEY
                    defaults={
                        'hmeromhnia_eis': clean(row.get('ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ')),
                        'syggrafeas': clean(row.get('ΣΥΓΓΡΑΦΕΑΣ')),
                        'koha': clean(row.get('ΣΥΓΓΡΑΦΕΑΣ KOHA')),
                        'titlos': clean(row.get('ΤΙΤΛΟΣ')),
                        'ekdoths': clean(row.get('ΕΚΔΟΤΗΣ')),
                        'ekdosh': clean(row.get('ΕΚΔΟΣΗ')),
                        'etosEkdoshs': clean(row.get('ΕΤΟΣ ΕΚΔΟΣΗΣ')),
                        'toposEkdoshs': clean(row.get('ΤΟΠΟΣ  ΕΚΔΟΣΗΣ')),
                        'sxhma': clean(row.get('ΣΧΗΜΑ')),
                        'selides': clean(row.get('ΣΕΛΙΔΕΣ')),
                        'tomos': clean(row.get('ΤΟΜΟΣ')),
                        'troposPromPar': clean(row.get('ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ')),
                        'ISBN': clean(row.get('ISBN')),
                        'sthlh1': clean(row.get('Στήλη1')),
                        'sthlh2': clean(row.get('Στήλη2')),
                    }
                )
                
                record_info = {
                    'ari8mos': ari8mos,
                    'titlos': obj.titlos,
                    'syggrafeas': obj.syggrafeas,
                }

                if was_created:
                    added.append(record_info)

                else:
                    updated.append(record_info)
                
            UploadLog.objects.create(
              user=request.user,
              filename=excel_file.name,
              rows_added=len(added),
              rows_updated=len(updated),
            )

            return render(request, 'upload_result.html', {
                'added': added,
                'updated': updated,
                'skipped': skipped,
            })

    else:
        form = UploadExcelForm()

    return render(request, 'upload_excel.html', {'form': form})
