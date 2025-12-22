from django.contrib import admin
from django.urls import path, include
from . import views
from .views import upload_excel, show_people, SignUpView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('people/', views.show_people, name='show_people'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('duplicates/', views.resolve_duplicates, name='resolve_duplicates'),
    path('duplicates/handle/', views.handle_duplicate, name='handle_duplicate'),
    path('person/edit/<str:pk>/', views.edit_person, name='edit_person'),
]
