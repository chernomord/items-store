from django.conf.urls import url, include
from django.views.generic import TemplateView
from store import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'items', views.ItemsViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Store Items API')

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include(router.urls)),
    url(r'^api/schema/$', schema_view),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]

