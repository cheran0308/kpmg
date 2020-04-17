from django.urls import path
from .views import Index, login, valid_data, add_new, invalid_data, get_wf_log, update_status, logout

urlpatterns = [
    path('', Index, name="Index"),
    path('login/', login, name="login"),
    path('add_new/', add_new, name="Add New"),
    path('approval/', valid_data, name="Valid Data"),
    path('created/', invalid_data, name="Invalid Data"),
    path('update_status/', update_status, name="Update Status"),
    path('get_wf_log/', get_wf_log, name="get_wf_log"),
    path('logout/', logout, name="get_wf_log")
]
