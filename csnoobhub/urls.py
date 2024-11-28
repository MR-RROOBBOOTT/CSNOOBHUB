from django.contrib import admin
from django.urls import path, include
from hello import views as hello_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_views.hello_world, name='root'),  # Root directs to Hello, World!
    path('blog/', include('blog.urls')),
    path('hello/', include('hello.urls')),
]