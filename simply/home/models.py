from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
    


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"



class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.name}"



class Buyer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"




class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_total = models.IntegerField(default=0)
    vote_percentage = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.writer.username}"
    
    @property
    def get_total(self):
        all_votes = self.review_set.all()
        all_up = all_votes.filter(type = 'up')

        all_count = all_votes.count()
        up_count = all_up.count()

        self.vote_total = all_count
        self.vote_percentage = (up_count/all_count)*100

        self.save()



class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
    )

    type = models.CharField(max_length=200, choices = VOTE_TYPE)
    comment = models.CharField(max_length=200, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.reviewer.username}"