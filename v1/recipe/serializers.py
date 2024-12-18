#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers
from rest_framework.serializers import ImageField
from rest_framework.settings import api_settings
from rest_framework.fields import SerializerMethodField

from v1.recipe.models import Recipe, SubRecipe
from v1.ingredient.serializers import IngredientGroupSerializer
from v1.recipe_groups.serializers import CourseSerializer, CuisineSerializer, SeasonSerializer, TagSerializer
from v1.recipe.mixins import FieldLimiter


class CustomImageField(ImageField):
    def to_representation(self, value):
        use_url = getattr(self, 'use_url', api_settings.UPLOADED_FILES_USE_URL)
        try:
            if not value:
                return None
        except:
            return None

        if use_url:
            if not getattr(value, 'url', None):
                # If the file has not been saved it may not have a URL.
                return None
            url = value.url
            request = self.context.get('request', None)
            if request is not None:
                return request.build_absolute_uri(url)
            return url

        return super(ImageField, self).to_representation(value)


class SubRecipeSerializer(serializers.ModelSerializer):
    """ Standard `rest_framework` ModelSerializer """
    slug = serializers.ReadOnlyField(source='child_recipe.slug')
    title = serializers.ReadOnlyField(source='child_recipe.title')

    class Meta:
        model = SubRecipe
        fields = [
            'child_recipe_id',
            'slug',
            'numerator',
            'denominator',
            'measurement',
            'title',
        ]


class MiniBrowseSerializer(FieldLimiter, serializers.ModelSerializer):
    """ Used to get random recipes and limit the return data. """
    pub_date = serializers.DateTimeField(read_only=True)
    photo_thumbnail = CustomImageField(required=False)
    seasons = SeasonSerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'slug',
            'title',
            'pub_date',
            'rating',
            'rating_count',
            'photo_thumbnail',
            'info',
            'seasons',
            'tags',
        ]


class RecipeSerializer(FieldLimiter, serializers.ModelSerializer):
    """ Used to create new recipes"""
    photo = CustomImageField(required=False)
    photo_thumbnail = CustomImageField(required=False)
    ingredient_groups = IngredientGroupSerializer(many=True)
    subrecipes = SerializerMethodField()
    seasons = SeasonSerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)
    course = CourseSerializer()
    cuisine = CuisineSerializer()
    pub_username = serializers.ReadOnlyField(source='author.username')
    pub_date = serializers.DateTimeField(read_only=True)
    update_author = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    update_username = serializers.ReadOnlyField(source='update_author.username')
    update_date = serializers.DateTimeField(read_only=True)

    def get_subrecipes(self, obj):
        try:
            subrecipes = SubRecipe.objects.filter(parent_recipe_id=obj.id)
            return [SubRecipeSerializer(subrecipe).data for subrecipe in subrecipes]
        except:
            return {}

    class Meta:
        model = Recipe
        fields = [
            'id',
            'photo',
            'photo_thumbnail',
            'ingredient_groups',
            'subrecipes',
            'seasons',
            'tags',
            'rating',
            'rating_count',
            'course',
            'cuisine',
            'pub_username',
            'pub_date',
            'update_author',
            'update_username',
            'update_date',
            'title',
            'slug',
            'info',
            'directions',
            'source',
            'prep_time',
            'cook_time',
            'servings',
            'public',
            'author',
        ]
