
from django.conf.urls import url, include
from rest_framework import routers
#from rest_framework import routers, serializers, viewsets
from balanca import views
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

router = routers.DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'groupo', views.GroupViewSet)
router.register(r'pesos', views.PesosViewSet)
router.register(r'mensagens', views.MensagemViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^balanca/', include('balanca.urls')),
    url(r'^autenticacao/', include('autenticacao.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

]
