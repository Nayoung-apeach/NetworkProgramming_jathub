from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # repo1.introduction_set.all => 나와관련된 자소서 다 가지고 오는 것 all 생략해도 됨.(그럼 전부 다 가져오는것이 아님)

    class Meta:
        verbose_name_plural = 'Repositories'

    def __str__(self):
        return self.name


class Introduction(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)  # intro1.repository idx랑 연결하는 것과 똑같은 역활을 한다.
    version = models.IntegerField(default=1)
    contents = models.TextField()
    access = models.IntegerField(default=1) #0이면 private 1이면 public

    # intro1.comment_set

    def __str__(self):
        return f'{self.version}{self.contents}'


class Comment(models.Model):
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)  # comment1.introduction
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
