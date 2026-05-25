# Create your views here.
#============================================= Function Based API Start ==============================================
"""
from django.shortcuts import render
from rest_framework.decorators import api_view
from society.models import Society
from .serializers import SocietySerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# GET all data and POST data

@api_view(['GET', 'POST'])
def society_list(request):

    if request.method == 'GET':

        society = Society.objects.all()
        serializer = SocietySerializer(society, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # POST new society
    elif request.method == 'POST':
        serializer = SocietySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# GET single data, UPDATE and DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def society_detail(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        raise Http404

    # GET single society
    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # UPDATE society
    elif request.method == 'PUT':
        serializer = SocietySerializer(society,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # DELETE society
    elif request.method == 'DELETE':
        society.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
"""

#======================================= Function Based API End ==============================================  













# ======================================class based API Start =================================================
"""
from django.shortcuts import render
from rest_framework.views import APIView
from society.models import Society
from .serializers import SocietySerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class SocietyAPIView(APIView):
    # get all data
    def get(self,request):
        society=Society.objects.all()
        serializer=SocietySerializer(society,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # post the data
    def post(self,request):
        serializer=SocietySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SocietyDetails(APIView):
    def get_object(self,pk):
        try:
            return Society.objects.get(pk=pk)
        except Society.DoesNotExist:
            raise Http404
            
    # get one data by id
    def get(self,request,pk):
        society=self.get_object(pk)
        serilaizer=SocietySerializer(society)
        return Response(serilaizer.data,status=status.HTTP_200_OK)
    
    # update 
    def put(self,request,pk):
        society=self.get_object(pk)
        serilaizer=SocietySerializer(society,data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data,status=status.HTTP_200_OK)
        return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # delete
    def delete(self,request,pk):
        society=self.get_object(pk)
        society.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
    """
# ============================================class based API End =================================================











#========================================== Mixin Based API Start ============================================== 
"""
from rest_framework import mixins,generics
from society.models import Society
from .serializers import SocietySerializer

class SocietyAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Society.objects.all()
    serializer_class=SocietySerializer
    
    
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class SocietyDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Society.objects.all()
    serializer_class=SocietySerializer
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)


"""







#  ===================================generics Based API Start ============================================== 
"""

from rest_framework import generics
from society.models import Society
from .serializers import SocietySerializer

# Single Api view for get all data and post data
# class SocietyAPIView(generics.ListAPIView,generics.CreateAPIView):

# combination Api view for get all and post data
class SocietyAPIView(generics.ListCreateAPIView):
    queryset=Society.objects.all()
    serializer_class=SocietySerializer

# Single Api view for get,update and delete one data
# class SocietyDetails(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):

# combination Api view for get,update and delete one data
class SocietyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Society.objects.all()
    serializer_class=SocietySerializer
    lookup_field= 'pk'
    
 """
#  ===================================generics Based API End ==============================================  








#  ===================================viewset Based API Start ==============================================  
"""
from rest_framework import viewsets
from society.models import Society
from .serializers import SocietySerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class SocietyViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Society.objects.all()
        serializer=SocietySerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=SocietySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        society=get_object_or_404(Society,pk=pk)
        serializer=SocietySerializer(society)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        society=get_object_or_404(Society,pk=pk)
        serializer=SocietySerializer(society,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk=None):
        society=get_object_or_404(Society,pk=pk)
        society.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
"""
#  ===================================viewset Based API End ==============================================  

 
 
 
 
 
 
 
 
#  ===================================Modelviewset Based API Start ==============================================  

from rest_framework import viewsets
from society.models import Society
from .serializers import SocietySerializer
# for custom pagination
from society.pagination import CustomPagination
# for custom filter
from society.filters import SocietyFilter

 

class SocietyViewset(viewsets.ModelViewSet):
    queryset=Society.objects.all()
    serializer_class=SocietySerializer
    
    # custm pagination
    pagination_class=CustomPagination
    
    # global filter
    # filterset_fields=['room_type']
    
    # custom filter
    filterset_class = SocietyFilter
    
    
 
#  ===================================Modelviewset Based API End ==============================================  





# =====================================BLog and comment nested serializer api using Genrics Start==============================================
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer
from rest_framework import generics

# for a search filter
from rest_framework.filters import SearchFilter
# by Ordering data by id asending order or desending order
from rest_framework.filters import OrderingFilter

class BlogsView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    # for seach the data in data fields 
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['blog_title','blog_body']
    # search_fields=['^blog_title']  # this is for search a data by first letter or name 
    
    # for Ordering the data
    ordering_fields=['id','blog_title']
     
    
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field='pk'
    
class CommentsView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    lookup_field='pk'
  
# =====================================BLog and comment nested serializer api using Genrics End==============================================  



