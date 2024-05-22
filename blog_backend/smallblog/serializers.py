from rest_framework import serializers

from .models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'post')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(required=False, many=True)
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'comments')
