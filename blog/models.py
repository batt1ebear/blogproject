from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



'''django创建一个类（表）会自动创建一个属性id'''



class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Category(models.Model):

    name= models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Post(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)#user在数据中自行创建

    #阅读量 非负整数
    viewed = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_viewed(self):
        self.viewed += 1
        self.save(update_fields=['viewed'])

