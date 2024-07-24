from django.urls import path,re_path, include
from salesdata import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r"^nus$", views.new_user_sugestion),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)