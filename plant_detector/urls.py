from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect  # <-- keep this

# Updated root redirect
def redirect_root(request):
    return redirect('detector:dashboard')  # <-- namespace added

urlpatterns = [
    path('', redirect_root),           # redirect from root
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # login/signup/logout
    path('detector/', include('detector.urls')), # dashboard & uploads
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
