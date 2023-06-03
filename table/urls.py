from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('report/', views.report, name='report'),
    path('add_excel_file/', views.add_excel_file, name='add_excel_file')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
