# models.py
from django.db import models
from django.conf import settings
# Giả sử bạn đã có model Course hoặc Lesson trước đó

class Question(models.Model):
    # Liên kết với bài học (Lesson) hoặc khóa học
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    # Lưu lịch sử nộp bài của user
    # enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE) 
    # Tùy thuộc vào schema của bạn, có thể liên kết với user/course
    score = models.IntegerField(default=0)
    passed = models.BooleanField(default=False)
