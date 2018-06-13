from django.db import models


class Article(models.Model):

    # 每次修改都必须执行下面命令
    # python manage.py makemigrations
    # python manage.py migrate
    title = models.CharField(max_length=255, default='title')
    name = models.TextField(null=True)
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    # 在admin管理界面中，显示标题信息
    def __str__(self):
        return self.title