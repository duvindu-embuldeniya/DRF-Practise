from django.db import models
# import uuid
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True) 
    long_intro = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media_profile_model/', blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    @property
    def imgUrl(self):
        try:
            return f"{self.image.url}"
        except Exception as ex:
            return '/static/images/static_profile_model/default.png'
    
    class Meta:
        ordering = ['-created']




class Skill(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.owner.username}"





class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
            return '/static/images/static_project_model/default.jpg'

    class Meta:
        ordering = ['-created']

    @property
    def vote_update(self):
        all_votes = self.review_set.all()
        total_up_count = all_votes.filter(value = 'up').count()

        total_count = all_votes.count()
        percentage = (total_up_count/total_count) * 100

        self.vote_total = total_count
        self.vote_ratio = percentage
        
        self.save()
    
    @property
    def checksum(self):
        query_set = self.review_set.all().values_list('owner__id', flat = True)
        return query_set




class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.project} | {self.value}"

    # class Meta:
    #     unique_together = [['owner', 'project']]





class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self):
        return f"{self.name}"
    


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    title = models.CharField(max_length=200)
    body = models.TextField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} -> {self.title}"  
    
    class Meta:
        ordering = ['status', '-created']
        # all false values first(status)