from django.db import models
from io import BytesIO
from PIL import Image

from django.core.files import File


class Category(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(blank=False)
    date = models.DateTimeField()
    Image = models.URLField()
    # cato = models.ForeignKey(
    #     BlogCategory, related_name='Blogs', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Videos(models.Model):
    category = models.ForeignKey(
        Category, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=False)
    date = models.DateTimeField()
    Image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    video_url = models.URLField(default='')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if (self.Image):
            return 'http://127.0.0.1:8000' + self.Image.url
        return ''

    def get_thumbnail(self):
        if (self.thumbnail):
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if (self.Image):
                self.thumbnail = self.make_thumbnail(self.Image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url

            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = image.open(image)
        img.covert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG', quality=75)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
