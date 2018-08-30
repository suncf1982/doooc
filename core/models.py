from django.db import models

# Create your models here.
class Resource(models.Model):
    class Meta:
        verbose_name = '资源管理'
        verbose_name_plural = '资源管理'

    name = models.CharField('资源名称', max_length=200)
    size =  models.IntegerField('资源大小', default=0)
    content_type = models.CharField('资源类型', max_length=200)
    storage = models.FileField('资源', upload_to='uploads/%Y/%m/%d/')
    create_at = models.DateTimeField('创建日期', editable=False, auto_now_add=True)
    update_at = models.DateTimeField('更新日期', editable=False, auto_now=True)

    def __str__(self):
        return self.name
