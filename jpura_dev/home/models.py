from django.db import models
# import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    source_link = models.CharField(max_length=200, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True) 
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    featured_image = models.ImageField(upload_to='media_project_model/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    @property
    def imgUrl(self):
        try:
            return f"{self.featured_image.url}"
        except Exception as ex:
            return '/static/static_project_model/default.jpg'

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.project} | {self.value}"


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self):
        return f"{self.name}"