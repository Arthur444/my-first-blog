from django.contrib import admin

from .models import produit, Image, Slide, windsurf, windsurfImage


"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
"""

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1



class produitAdmin(admin.ModelAdmin):
    list_display = ('produit_titre', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['produit_titre']

    fieldsets = [
                 (None,               {'fields': ['produit_titre']}),

                 (None,               {'fields': ['produit_description']}),

                 (None,               {'fields': ['produit_text']}),
                 (None,               {'fields': ['photo']}),

                 ('Movie (optional)',               {'fields': ['produit_video']}),

                 ('Date information', {'fields': ['pub_date']}),
                 

                                  ]
                                  
                                  
                                  
    inlines = [ImageInline]





admin.site.register(produit, produitAdmin)

































class SlideAdmin(admin.ModelAdmin):
    list_display = ('slide_titre', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['slide_titre']

    fieldsets = [
                 (None,               {'fields': ['slide_titre']}),


                 (None,               {'fields': ['photo']}),


                 ('Date information', {'fields': ['pub_date']}),
                 

                                  ]
                                  
                                  
                                  

admin.site.register(Slide, SlideAdmin)


























class windsurfImageInline(admin.TabularInline):
    model = windsurfImage
    extra = 1





class windsurfAdmin(admin.ModelAdmin):
    list_display = ('windsurf_titre', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['windsurf_titre']

    fieldsets = [
                 (None,               {'fields': ['windsurf_titre']}),

                 (None,               {'fields': ['windsurf_description']}),

                 (None,               {'fields': ['windsurf_text']}),
                 (None,               {'fields': ['photo']}),

                 ('Movie (optional)',               {'fields': ['windsurf_video']}),

                 ('Date information', {'fields': ['pub_date']}),
                 

                                  ]
                                  
                                  
                                  
    inlines = [windsurfImageInline]





admin.site.register(windsurf, windsurfAdmin)







"""

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
                 
                 (None,               {'fields': ['product_text']}),
                 (None,               {'fields': ['photo']}),
                 ('Date information', {'fields': ['pub_date']}),
                 ]

admin.site.register(Product, ProductAdmin)



    class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    
    
    
    
    ('Product', {'fields': ['product_titre']}),
    """

#inlines = [ImageInline]

