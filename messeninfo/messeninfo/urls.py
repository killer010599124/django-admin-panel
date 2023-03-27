
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from airport import views as airportViews
from messezentren import views as messezentrenViews
from messebranchen import views as messenbranchenViews

from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    # path('rosetta', include('rosetta.urls')),
    path('Hotels-Expo-Centre-Sharjah-Sharjah-ZS<id>', messezentrenViews.Hotels),
    path('airport/', airportViews.home, name='home'),
    path('hrach/', include('hrach.urls')),
    path('messezentren/', include('messezentren.urls')),
    
    path('messebranchen/', include('messebranchen.urls')),
    # path('messebranchen/', messenbranchenViews.HomeView, name='home'),
    
)   