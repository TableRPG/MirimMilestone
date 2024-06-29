# myproject/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('게시판.urls')),
    path('설명서/', include('설명서.urls')),
    path('', include('설명서.urls')),  # 메인 화면을 category_list로 설정
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
