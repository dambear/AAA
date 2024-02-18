from django.contrib import admin
from django.urls import path, include

from .views.epmd.views import index


from .views.epmd.ojt_view import epmd_ojt, add_data_ojt, update_data_ojt, delete_data_ojt, view_data_ojt

from .views.auth.auth import login_page, logout_page

from django.contrib.auth import views as auth_views

urlpatterns = [
    # for auto reload
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    #
    #
    # auth
    path("login", login_page, name="login_page"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout", logout_page, name="logout_page"),
    #
    #
    #
    path("", index, name="index"),
    #
    #
    #
    path("epmd_ojt/", epmd_ojt, name="epmd_ojt"),
    path("epmd_ojt/add_data_ojt/", add_data_ojt, name="add_data_ojt"),
    path("epmd_ojt/update_data_ojt/<int:ojt_id>/", update_data_ojt, name="update_data_ojt",),
    path("epmd_ojt/delete_data_ojt/<int:ojt_id>/", delete_data_ojt, name="delete_data_ojt",),
    path("epmd_ojt/view_data_ojt/<int:ojt_id>/", view_data_ojt, name="view_data_ojt"),
]
