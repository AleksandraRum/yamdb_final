from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include, path
from rest_framework import permissions
from .views import debug_send_email
from rest_framework.routers import SimpleRouter

from .views import (AdminViewSet, APITokenCreate, APIUserCreate,
                    CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

router_v1 = SimpleRouter()

app_name = 'api'

router_v1.register(
    'users',
    AdminViewSet
)

router_v1.register(
    'categories',
    CategoryViewSet,
    basename='сategories'
)
router_v1.register(
    'titles',
    TitleViewSet,
    basename='titles'
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

schema_view = get_schema_view(
    openapi.Info(
        title="YaMDb API",
        default_version='v1',
        description="Документация для API YaMDb",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

VERSION_PARAM = 'api/v1'

auth_patterns = [
    path('signup/', APIUserCreate.as_view()),
    path('token/', APITokenCreate.as_view()),
]

urlpatterns = [
    path(f'{VERSION_PARAM}/', include(router_v1.urls)),
    path(f'{VERSION_PARAM}/auth/', include(auth_patterns)),
]

urlpatterns += [
    path(f'{VERSION_PARAM}/debug-email/', debug_send_email),
]

urlpatterns += [
    path('swagger/',
        schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'),
    path('redoc/',
        schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
