from django.db import models
from django.conf import settings

# Các model có sẵn (Course, Lesson, Enrollment,...) giữ nguyên của bạn
# Dưới đây là phần code bổ sung chuẩn cho Bài kiểm tra:

class Question(models.Model):
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
    # Đã thêm đầy đủ enrollment và choices theo yêu cầu của hệ thống chấm điểm
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
