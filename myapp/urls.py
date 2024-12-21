from myapp.views import Home, ProfileList, ProfileCreate, Watch, ShowMovieDetail, ShowMovie
from django.urls import path

app_name = 'myapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<uuid:profile_id>/', Watch.as_view(), name='watch'),
    path('movie/detail/<uuid:movie_id>/', ShowMovieDetail.as_view(), name='show_det'),
    path('movie/play/<uuid:movie_id>/', ShowMovie.as_view(), name='play'), 
]


