from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    # path('logout', auth_views.auth_logout, name='logout'),
    path('', views.menuScreenView, name="menu"),
    path('<int:level_num>/start', views.levelTitleScreenView, name="start_level"),
    path('<int:level_num>/editor', views.levelEditorView, name="editor"),
]