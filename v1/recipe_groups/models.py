#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from v1.common.db_fields import AutoSlugField


class Course(models.Model):
    """
    Django Model to hold Courses.
    Courses have a one to Many relation with Recipes.
    Each Recipe will be assigned a Course.
    :title: = Title of the Course
    :slug: = Slug of the Course
    :author: = Creator of the Course
    """
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title


class Cuisine(models.Model):
    """
    Django Model to hold Cuisines.
    Cuisines have a one to Many relation with Recipes.
    Each Recipe will be assigned a Cuisine.
    :title: = Title of the Cuisine
    :slug: = Slug of the Cuisine
    :author: = Creator of the Cuisine
    """
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Season(models.Model):
    """
    Django Model to hold Seasons.
    Seasons have a one to Many relation with Recipes.
    Each Recipe will be assigned a Season.
    :title: = Title of the Season
    :slug: = Slug of the Season
    """
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)

    def __str__(self):
        return '%s' % self.title

    def recipe_count(self):
        return self.recipe_set.filter(shared=0).count()


class Tag(models.Model):
    """
    Django Model to hold Tags.
    Tags have a Many to Many relation with Recipes.
    Each Recipe can have many Tags.
    :title: = Title of the Tag
    :slug: = Slug of the tag
    """
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)

    def __str__(self):
        return '%s' % self.title

    def recipe_count(self):
        return self.recipe_set.filter(shared=0).count()
