from rest_framework import serializers
from .models import AwardsMerch, ProjectMerch


class ProfileMerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsMerch
        fields = ('id', 'name', 'profile_pic', 'bio')


class ProjectMerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMerch
        fields = ('id', 'image', 'project_name', 'user', 'url')