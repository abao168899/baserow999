from django.conf.urls import url

from baserow.contrib.database.views.registries import view_type_registry

from .views import ViewsView, ViewView, ViewFiltersView, ViewFilterView


app_name = 'baserow.contrib.database.api.views'

urlpatterns = view_type_registry.api_urls + [
    url(r'table/(?P<table_id>[0-9]+)/$', ViewsView.as_view(), name='list'),
    url(
        r'filter/(?P<view_filter_id>[0-9]+)/$',
        ViewFilterView.as_view(),
        name='filter_item'
    ),
    url(r'(?P<view_id>[0-9]+)/$', ViewView.as_view(), name='item'),
    url(
        r'(?P<view_id>[0-9]+)/filters/$',
        ViewFiltersView.as_view(),
        name='list_filters'
    ),
]
