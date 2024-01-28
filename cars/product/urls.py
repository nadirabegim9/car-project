from django.urls import path
from .views import *

urlpatterns = [
    path('', CarView.as_view(), name='carView'),
    path('<int:pk>', CarDetailView.as_view(), name='carDetailView'),
    path('create/', CarCreateView.as_view(), name='carCreateView'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='carUpdateView'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='carDeleteView'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='commentCreateView'),
    path('cat/', CategoryView.as_view(), name='categoryView'),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view(), name='categoryDeleteView'),
    path('cat/create/', CategoryCreateView.as_view(), name='categoryCreateView'),
    path('marka/', MarkaView.as_view(), name='markaView'),
    path('marka/<int:pk>/delete/', MarkaDeleteView.as_view(), name='markaDeleteView'),
    path('marka/create/', MarkaCreateView.as_view(), name='markaCreateView'),
]