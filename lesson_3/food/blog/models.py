from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=20, verbose_name='Логин')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='email', max_length=50)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return f'{self.username}'


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок',
                             db_index=True)
    content = models.TextField(verbose_name='Содержание', default='')
    published_at = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True)
    status_choices = [
        ('a', 'Active'),
        ('i', 'Inactive')
    ]
    activity_flag = models.CharField(max_length=1, choices=status_choices,
                                     default='i')
    author = models.ForeignKey(Author, verbose_name='автор', on_delete=models.CASCADE)

    class Meta:
        db_table = 'news'
        ordering = ['-published_at']
        permissions = [
            ('can_publish', 'Может опубликовать новость')
        ]

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):

    email = models.EmailField(max_length=50, verbose_name='email')
    username = models.CharField(max_length=20, verbose_name='логин')
    comment = models.TextField(verbose_name='комментарий')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='новость')

    class Meta:
        db_table = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'{self.email}'




