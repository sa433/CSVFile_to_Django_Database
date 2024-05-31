
from django.contrib import admin
from django.urls import path
from myapp.views import home, import_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('import_student', import_student, name='import_student'),
]
