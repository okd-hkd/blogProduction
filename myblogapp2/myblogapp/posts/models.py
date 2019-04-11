from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    #title = MarkdownxField('Title', help_text='Markdown')
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/', blank=True)  # ドメイン + MEDIA_URL + upload_to に画像を保存してpathをDBに保存
    # image = models.ImageField()
    # body = models.TextField()
    body = MarkdownxField('body', help_text='Markdown')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:40]

    def body_to_markdown(self):
        return markdownify(self.body)
