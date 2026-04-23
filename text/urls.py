from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('timetable/', views.timetable, name='timetable'),
    path('syllabus/', views.syllabus_view, name='syllabus'),
    path('add/', views.add_syllabus, name='add_syllabus'),
    path('delete/<int:syllabus_id>/', views.delete_syllabus, name='delete_syllabus'),
    path('edit/<int:syllabus_id>/', views.edit_syllabus, name='edit_syllabus'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)