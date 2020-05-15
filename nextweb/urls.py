"""nextweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from techbee.urls import router

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve  #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('techbee/',include("techbee.urls")),
    path('auth/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/',include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]


from django.conf.urls import handler500

# 自作の 500 エラーハンドラー。
handler500 = views.my_error_handler
#from django.conf import settings  # 追加
#from django.conf.urls.static import static # 追加

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
