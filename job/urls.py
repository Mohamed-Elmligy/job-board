from django.urls import include, path

urlpatterns = [
    path('jobs/', include('job.urls')),
]
