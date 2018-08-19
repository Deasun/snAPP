from django.urls import include, path
from accounts.views import logout, login, registration, user_profile, edit_profile, delete_profile
from accounts import url_reset


urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
    path('profile/<int:id>', user_profile, name="profile"),
    path('password_reset/', include(url_reset)),
    path('edit_profile/', edit_profile, name="edit_profile"),
    path('delete_profile/<int:id>', delete_profile, name="delete_profile"),
]