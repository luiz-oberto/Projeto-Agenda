from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'), 
    path('search/', views.search, name='search'),

    # PADRÃO DE URL'S PARA O SITE
    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    # path('contact/<int:contact_id>/update/', views.contact, name='contact'),
    # path('contact/<int:contact_id>/delete/', views.contact, name='contact'),

    # user (CRUD)
    # path('user/contact/<int:contact_id>/detail/', views.contact, name='contact'),
    # path('user/create/', views.contact, name='contact'),
    # path('user/<int:contact_id>/update/', views.contact, name='contact'),
    # path('user/<int:contact_id>/delete/', views.contact, name='contact'),
]
