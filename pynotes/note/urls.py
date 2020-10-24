from django.urls  import path

from . import views

app_name = "note"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/",views.PostDetailView.as_view(), name="detail"),
]