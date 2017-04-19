from django.contrib import admin
from blog.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin): #관리자페이지에서 Post객체를 어떻게 보여줄지 정의하는 클래스
    list_display = ('title','modify_date') #제목과 수정시간만 보여줘라
    list_filter = ('modify_date',) # 컬럼 필터를 지정
    search_fields = ('title','content') # 검색박스를 표시하고 입력된 단어는 제목과 내용에서 찾는다. 좋은 기능이구만
    prepopulated_fields = {'slug':('title',)} # slug필드는 title필드를 이용해 미리 채워지도록 함

admin.site.register(Post,PostAdmin) # Post와 PostAdmin 클래스를 관리자페이지에 등록한다.
