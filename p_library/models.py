from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Friend(models.Model):
    full_name = models.TextField()
    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.CharField(max_length=100, default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=0.00)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True,)
    friend = models.ManyToManyField(Friend, blank=True, related_name='friends')
    borrowed_book_count = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title
