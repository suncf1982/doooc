from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from .enums import TECH_STACK
from datetime import datetime

# Create your models here.


class Doc(models.Model):
    class Meta:
        verbose_name = '文档'
        verbose_name_plural = '文档'
    title = models.CharField('标题', max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        verbose_name="作者",
        related_name='doc_authors',
        null=True,
    )
    tech_stack = models.CharField('技术栈', max_length=50, choices=TECH_STACK, default='OTHER', null=True, blank=True)
    content = models.TextField('内容')
    tags = TaggableManager(verbose_name="标签")
    download_times = models.IntegerField('下载次数', default=0)
    published = models.BooleanField('发布', default=False, editable=True)
    create_at = models.DateTimeField('创建日期', editable=False, auto_now_add=True)
    update_at = models.DateTimeField('更新日期', editable=True, default=timezone.now)

    def __str__(self):
        return self.title

    def get_tags_display(self):
        return self.tags.names()

class PopularKeywordManager(models.Manager):
    def addKeyword(self, word):
        if len(word) > 10:
            return
        queryset=  self.get_queryset().filter(keyword=word)
        if len(queryset) == 0:
            super(PopularKeywordManager, self).create(keyword=word)
        else:
            obj = queryset[0]
            obj.count = obj.count+1
            obj.save()

class PopularKeyword(models.Model):
    class Meta:
        verbose_name = '热门搜索'
        verbose_name_plural = '热门搜索'
    keyword = models.CharField('关键则', max_length=200, unique=True)
    count = models.IntegerField('次数', default=1)
    update_at = models.DateTimeField('更新日期', editable=False, auto_now=True)
    objects = PopularKeywordManager()
    def __str__(self):
        return self.keyword

class DocTemplate(models.Model):
    class Meta:
        verbose_name = '文档模板'
        verbose_name_plural = '文档模板'
    name = models.CharField('模板名称', max_length=200, unique=True)
    storage = models.FileField('存放位置', upload_to='templates/%Y/%m/%d/')
    preview_image = models.ImageField('预览图', upload_to='uploads/%Y/%m/%d/')
    usage_times = models.IntegerField('应用次数', default=0)
    create_at = models.DateTimeField('创建日期', editable=False, auto_now_add=True)
    update_at = models.DateTimeField('更新日期', editable=False, auto_now=True)

    def __str__(self):
        return self.name
