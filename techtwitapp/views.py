from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from .models import RecordPost

from django.views.generic import FormView

from django.urls import reverse_lazy

from .forms import ContactForm

from django.contrib import messages

from django.core.mail import EmailMessage

from django.views.generic import CreateView

from .forms import RecordPostForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.views.generic import DeleteView


class IndexView(ListView):
    
    template_name='index.html'
    
    context_object_name='orderby_records'
    
    queryset=RecordPost.objects.order_by('-posted_at')
    
    paginate_by=4
    

class RecordDetail(DetailView):
    template_name='post.html'
    
    model=RecordPost

class ClangView(ListView):
    template_name='C_C++_list.html'
    
    model=RecordPost
    
    context_object_name='Clang_records'
    
    queryset=RecordPost.objects.filter(
        category='C/C++').order_by('-posted_at')
    
    paginate_by=2
    
class PythonView(ListView):
    template_name='python_list.html'
    
    model=RecordPost
    
    context_object_name='python_records'
    
    queryset=RecordPost.objects.filter(
        category='Python').order_by('-posted_at')
    
    paginate_by=2
    
class Kotlin_JavaView(ListView):
    template_name='Kotlin_Java_list.html'
    
    model=RecordPost
    
    context_object_name='Kotlin_Java_records'
    
    queryset=RecordPost.objects.filter(
        category='Kotlin/Java').order_by('-posted_at')
    
    paginate_by=2

class othersView(ListView):
    template_name='others_list.html'
    
    model=RecordPost
    
    context_object_name='その他_records'
    
    queryset=RecordPost.objects.filter(
        category='その他').order_by('-posted_at')

class ContactView(FormView):
    template_name='contact.html'
    
    form_class=ContactForm
    
    success_url=reverse_lazy('techtwitapp:contact')
    
    def form_valid(self, form):
        
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        
        subject='お問い合わせ: {}'.format(title)
        
        message=\
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
        
        from_email='hachibo38@gmail.com'
        to_list=['hachibo38@gmail.com']
        
        message=EmailMessage(subject=subject,
                             body=message,
                             from_email=from_email,
                             to=to_list,
                             )
        
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました')
        
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CreateRecordView(CreateView):
    form_class=RecordPostForm
    template_name="post_record.html"
    success_url=reverse_lazy('techtwitapp:post_done')
    
    def form_valid(self, form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        
        return super().form_valid(form)
          

class PostSuccessView(TemplateView):
    template_name='post_success.html'
    

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=5
    
    def get_queryset(self):
        
        queryset=RecordPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        
        return queryset
    
class RecordDeleteView(DeleteView):
    model=RecordPost
    template_name='record_delete.html'
    success_url=reverse_lazy('techtwitapp:mypage')
    
    def delete(self, request, *args, **kwargs):
        
        return super().delete(request, *args, **kwargs)






