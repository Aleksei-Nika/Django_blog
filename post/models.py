from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Введите заголовок поста'
    )
    
    content = models.TextField(
        verbose_name='Содержание',
        help_text='Введение текста поста'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True, #Фиксирует время создания поста
        verbose_name='Дата создания'
    )
    
    update_at = models.DateTimeField(
        auto_now=True, #Фиксирует время обновления (редактирования) поста
        verbose_name='Дата обновления'
    )
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        # user.posts.all()
        related_name='posts',
        null=True, # может содержать значение null
        blank=True # может быть пустым
    )
    
    def __str__(self):
        return self.title
    
    def can_edit(self, user):
        if not user.is_authenticated:
            return False
        return user == self.author or (hasattr(user, 'profile') and user.profile.is_moderator)
    
    def can_delete(self, user):
        if not user.is_authenticated:
            return False
        return user == self.author or (hasattr(user, 'profile') and user.profile.is_moderator)
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        
        ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='comments' #post.comments.all()
    )
    text = models.TextField(verbose_name='Текст коментария')
    
    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            verbose_name='Автор',
            related_name='comments' # user.comments.all() 
        )
    
    created_at = models.DateTimeField(
            auto_now_add=True, #Фиксирует время создания поста
            verbose_name='Дата создания'
        )
        
    def __str__(self):
        return f'Комментарий от {self.author} к {self.post.title}'
    
    def can_delete(self, user):
        if not user.is_authenticated:
            return False
        return user == self.author or (hasattr(user, 'profile') and user.profile.is_moderator)
    
    class Meta:
        verbose_name = 'Комментарий',
        verbose_name_plural = 'Коментарии',
        ordering = ['-created_at']