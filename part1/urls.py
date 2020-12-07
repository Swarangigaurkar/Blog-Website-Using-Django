from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="Homepage"),
    path('postdetail',views.postdetail,name="postdetail"),
    path('createpost',views.createpost,name="createpost"),
    path('profile',views.profile,name="profile"),
    path('editpost',views.editpost,name="editpost"),
    path('puborsaveeditpost',views.puborsaveeditpost,name="publisheditedpost"),

] 