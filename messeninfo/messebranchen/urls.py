from django.urls import path
from .views import HomeView, CategoryView, NewBranchenView, EditBranchenView, DeleteBranchen
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', HomeView, name='home'),
    path('category/<int:cats>/', CategoryView, name='category'),
    path('add/', NewBranchenView, name = 'new'),
    # path('addForm', )
    path('edit/<int:cats>/' , EditBranchenView, name = 'edit'),
    path('delete/<int:cats>', DeleteBranchen, name = 'delete')
    ]
    
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()