from django.urls import path 
from .views import Reg, log, hello
urlpatterns = [
    path('hello/',hello, name="hello-page"),
    path('reg/',Reg, name="reg-page"),
    path('log/',log, name="log-page")

]