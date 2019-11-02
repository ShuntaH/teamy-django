from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SearchForm, CustomUserCreationForm
from .models import User


class IndexView(generic.ListView):
    model = User

    def get_context_data(self, **kwargs):
        # テンプレートに渡す辞書の作成
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)  # 元の辞書にformを追加
        return context

    def get_queryset(self):
        # テンプレートに渡すmember_listを作成する
        form = SearchForm(self.request.GET)
        """Return True if the form has no errors, or False otherwise."""
        form.is_valid()  # これをしないとcleaned_dataができない
        '''
        if form.is_valid()と書いていたことが多いが、今回はmodelでrequiredをfalseに
        してあるのでis_validは必ずTrueになるがis_valid()をしないとformのcleaned_data
        にアクセスできない
        '''
        queryset = super().get_queryset()
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)

        '''
        引数のdepartmentはmodel Memberのfield名
        代入するのはdepartment = form.cleaned_data['department']
        '''

        club = form.cleaned_data['club']
        if club:
            queryset = queryset.filter(club=club)

        return queryset


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('teamy:signin')
    template_name = 'teamy/signup.html'

    # def post(self, request, *args, **kwargs):
    #     response = super().post(self)
    #     messages.success(self.request, 'Your account was created successfully')
    #     return response
