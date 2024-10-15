from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import BlogModel
from .serializers import BlogModelSerializer, UpdateBlogModelSerializer
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action



class BlogViews(ViewSet):


            # list all the blogs
    def list(self,request):
        queryset = BlogModel.objects.all()
        serializer = BlogModelSerializer(queryset,many=True)
        return Response(serializer.data)
    

    # create a blog

    def create(self,request):
        serializer = BlogModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 
    # retriving only one blog
    def retrieve(self, request, pk=None):
        queryset = BlogModel.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BlogModelSerializer(user)
        return Response(serializer.data)

    # update a blog
    def update(self, request, pk=None):
     
        try:
            blog = BlogModel.objects.get(blog_id=pk)
        except BlogModel.DoesNotExist:
            raise NotFound(detail=f'blog with id {pk} not found')
        
        serializer = BlogModelSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # partially update a blog
    def partial_update(self, request, pk=None):

            try:
                blog = BlogModel.objects.get(blog_id=pk)
            except BlogModel.DoesNotExist:
                raise NotFound(detail=f'Blog with id {pk} not found')
            content = request.data.get('content')
            if content is None:
                raise NotFound(detail='No content to update found')
            update_data = {'content': content}

            # Pass only the filtered data to the serializer
            serializer = UpdateBlogModelSerializer(blog, data=update_data, partial=True)

            # Validate and save the serializer
            if serializer.is_valid():
                serializer.save()
                return Response({"success": serializer.data}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        # delte a blog
    def destroy(self,request, pk=None):
        try:
            blog = BlogModel.objects.get(blog_id=pk)
        except BlogModel.DoesNotExist:
            raise NotFound(detail=f'blog with id {pk} not found')
        blog.delete()
        return Response({"success":'blog removed'},status=status.HTTP_204_NO_CONTENT)



    @action(detail=False, methods=['get'], url_path='get_blogs_by_criteria')
    def get_blogs_by_criteria(self, request):
        match = self.request.query_params.get('match')
        if not match:
            return Response({'error': 'Match word not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        blogs = BlogModel.objects.filter(content__icontains=match)
        if not blogs.exists():
            raise NotFound(detail=f'No blogs match the criteria: {match}')

        serializer = BlogModelSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)