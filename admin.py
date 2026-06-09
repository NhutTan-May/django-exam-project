from django.contrib import admin
# Đã import đủ 7 class theo yêu cầu
from .models import Course, Lesson, Question, Choice, Submission, Instructor, Learner

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'lesson', 'grade']

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')

# Register toàn bộ 7 class
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
