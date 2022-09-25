from django.urls import path
from . import views

app_name='techtwitapp'

urlpatterns=[
    path('',views.IndexView.as_view(), name='index'),
    
    path(
        'record-detail/<int:pk>/',
        views.RecordDetail.as_view(),
        name='record_detail'
        ),
    
    path(
        'C_C++_list/',
        views.ClangView.as_view(),
        name='C_C++_list'
        ),
    
    path(
        'python_list/',
        views.PythonView.as_view(),
        name='python_list'
        ),
    
    path(
        'Kotlin_Java_list',
        views.Kotlin_JavaView.as_view(),
        name='Kotlin_Java_list'
        ),
    
    path(
        'others_list',
        views.othersView.as_view(),
        name='others_list'
        ),
    
    #問い合わせ
    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'
        ),
    
    path('post_record/',views.CreateRecordView.as_view(), name='post_record'),
    
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    
    path('techtwitapp/<int:pk>/delete/', views.RecordDeleteView.as_view(), name='record_delete'),
]