from django.contrib import admin
from . models import Category, Article , Comment



admin.site.register(Category)

class Articlemodel(admin.ModelAdmin):
    list_display = ["__str__", "category" , "lead", "lead2", "lead3"]
    list_editable = ["lead", "lead2", "lead3"]
    list_filter = ["lead","lead2","lead3", "category"]
    search_fields = ["__str__", "category"]
    list_per_page = 10
    class Meta:
        Model = Article
admin.site.register(Article , Articlemodel)

class CommentModel(admin.ModelAdmin):
    list_display = ["__str__","name"]
    list_per_page = 10
    class Meta:
        Model = Comment
admin.site.register(Comment , CommentModel)