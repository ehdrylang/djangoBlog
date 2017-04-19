from __future__ import unicode_literals #파이썬2,3 문자열 처리 호환
from django.db import models
from django.core.urlresolvers import reverse #reverse 함수는 URL패턴을 만들어주는 함수
from django.utils.encoding import python_2_unicode_compatible #파이썬2,3 문자열 처리 호환

# Create your models here.
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE',max_length=50)
    slug = models.SlugField('SLUG',unique=True,allow_unicode=True,help_text='one word for title alias') #allow_unicode하면 한글처리가능
    description = models.CharField('DESCRIPTION',max_length=100,blank=True,help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date',auto_now_add=True)#antu_now_add = 객체가 생성될 때 자동 기록
    modify_date = models.DateTimeField('Modify_Date',auto_now=True)#auto_now = 데이터베이스에 저장될 때 자동 기록

    class Meta: #필드 외에 필요한 파라미터는 메타클래스에 정의
        verbose_name = 'post' #테이블 단수 별칭
        verbose_name_plural = 'posts' #테이블 복수 별칭
        db_table = 'my_post' #데이터베이스에 저장되는 테이블 이름을 'my_post' 로함
        ordering = ('-modify_date',) # 모델객체 리스트 출력시 정렬을 modify_date기준 내림차순

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=(self.slug,)) # 장고 내장 함수

    def get_previous_post(self):
        return self.get_previous_by_modify_date() #장고 내장 함수

    def get_next_post(self):
        return self.get_next_by_modify_date() #장고 내장 함수
