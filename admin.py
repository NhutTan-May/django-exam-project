# admin.py
from django.contrib import admin
# Đảm bảo import đủ 7 class theo yêu cầu (ví dụ dưới đây là 6 class từ models + admin là 7)
from .models import Course, Lesson, Question, Choice, Submission, Enrollment 

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # Hiển thị sẵn 3 ô trống để nhập đáp án

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson', 'grade')

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'course')

# Đăng ký các model
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
# Nhớ register các model khác của bạn để chúng hiện lên trang Admin
