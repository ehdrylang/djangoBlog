from django.contrib import admin
from photo.models import Album,Photo
# Register your models here.
class PhotoInline(admin.StackedInline): #앨범과 포토의 관계 1:N 즉 앨범보여줄때 연결된 사진도 보여주는 방식
    #    StackedInline은 세로로 나열, TabularInline은 행으로 나열 table스타일
    model = Photo
    extra = 2

class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline] # 앨범객체를 보여줄때 포토인라인클래스에서 정의한 사항도 같이 보여준다.
    list_display = ('name','description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','upload_date')

admin.site.register(Album,AlbumAdmin)
admin.site.register(Photo,PhotoAdmin)
