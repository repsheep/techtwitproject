from django.db import models
from accounts.models import CustomUser

class RecordPost(models.Model):
    
    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
        null=True
        )
    
    CATEGORY=(('C/C++','C/C++'),
              ('Python','Python'),
              ('Kotlin/Java','Kotlin/Java'),
              ('その他','その他')
              )
    
    title=models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    
    question=models.TextField(
        verbose_name='質問'
        )
    
    answer=models.TextField(
        verbose_name='回答'
        )
    
    posted_at=models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    
    category=models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
        )
    
    def __str__(self):
        
        return self.title