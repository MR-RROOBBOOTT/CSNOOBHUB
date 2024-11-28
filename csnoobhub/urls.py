from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Set pages as the root app
    path('blog/', include('blog.urls')),
    path('hello/', include('hello.urls')),
]