from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blog.models import Post
from django.views.generic.base import TemplateView
from tagging.models import Tag, TaggedItem #추가
from tagging.views import TaggedObjectList #추가

from django.views.generic.edit import FormView #폼 제네릭 뷰
from blog.forms import PostSearchForm # 검색폼으로 사용할 사용자정의 클래스임포트
from django.db.models import Q # 검색기능에 필요함
# 인증기능
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'

class HomeView(TemplateView):
    template_name = 'home.html'

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

class SearchFormView(FormView): # FormView는 get요청으로 왔을때 보여줄 폼 설정하고 폼에서 사용자입력이 완료되면 post로 가면서 유효성체크
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'
    #form_valid는 POST로 왔을 때 에러가 없으면 실행될 함수
    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word'] # post요청에 'search_word' 파라미터를 추출, 그워드를 schWord에 저장
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        #icontains 연산자는 대소문자를 구분않고 단어 포함되어있는지 검사
        #distinct 함수는 중복 제외 결국 서로다른 레코드객체들을 포스트리스트에 저장
        context = {} # 이제 템플릿에 보내줄 컨텍스트변수를 사전 형식으로 정의
        context['form'] = form #PostSearchForm을 컨텍스트변수 form에 지정
        context['search_term'] = schWord # 검색어도 넘김
        context['object_list'] = post_list # 검색결과도 넘김
        return render(self.request, self.template_name, context) #render함수덕분에 리다이렉트 안됨 FormView가 원래 리다이렉트함
        # render가 템플릿파일이랑 컨테스트변수를 처리해서 최총적으로 HttpResponse객체를 반환
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
