from django.urls import path,include
from . import views



# =============viewset Based API=======================
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('society',views.SocietyViewset,basename='society')
# =============viewset Based API======================= 




# =============Modelviewset Based API=======================
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('society',views.SocietyViewset,basename='society')
# =============Modelviewset Based API======================= 



urlpatterns = [
    
    # =============Function Based API=======================
    # path('society/', views.society_list),
    # path('society/<int:pk>/', views.society_detail),
    # =============Function Based API=======================

    
    
    # =============class based API=======================
    # path('society/',views.SocietyAPIView.as_view()),
    # path('society/<int:pk>/',views.SocietyDetails.as_view()),
    # =============class based API=======================
    
    
    
    # =============Mixin Based API=======================
    #  path('society/',views.SocietyAPIView.as_view()),
    #  path('society/<int:pk>/',views.SocietyDetails.as_view()),
    # =============Mixin Based API=======================
    
    
    # =============genrics Based API=======================
    #  path('society/',views.SocietyAPIView.as_view()),
    #  path('society/<int:pk>/',views.SocietyDetails.as_view()),
    # =============genrics Based API=======================
    
    # =============viewset Based API=======================
    # path('',include(router.urls)),
    # =============viewset Based API======================= 
    
   
    # =============Modelviewset Based API=======================
    path('',include(router.urls)),
    # =============Modelviewset Based API=======================
    
    
    
    
    
    # =============BLog and comment nested serializer api=======================
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view()),
    # =============BLog and comment nested serializer api=======================

    
    
       
]
