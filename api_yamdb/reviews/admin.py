from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "year",
        "category",
        "description",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("text", "score", "pub_date", "author", "title")
    search_fields = (
        "text",
        "pub_date",
        "author",
        "score",
    )
    list_filter = (
        "pub_date",
        "score",
    )
    empty_value_display = "-пусто-"

    @admin.register(Comment)
    class CommentAdmin(admin.ModelAdmin):
        list_display = ("review", "author", "text", "pub_date")

    list_display_links = ("text",)
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"
