
from django.urls import path
from users_apis import views
urlpatterns = [
    path('',views.NoteList.as_view()),
    path('<int:pk>/',views.NoteDetail.as_view())
]