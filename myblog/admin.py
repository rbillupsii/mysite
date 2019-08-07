from django.contrib import admin
from myblog.models import Post, Category

class InlineModelAdmin(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    inline = [InlineModelAdmin, ]
    exclude = ('posts', )

admin.site.register(Post, CategoryAdmin)
admin.site.register(Category, CategoryAdmin)
