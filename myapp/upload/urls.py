from django.conf.urls import url

from upload import views


urlpatterns = [
    url(r'^user_photo/', views.upload_photo),
]
