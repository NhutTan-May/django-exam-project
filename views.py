# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Logic chấm điểm sẽ lặp qua các câu hỏi và kiểm tra đáp án user gửi lên
        # Đây là khung ví dụ cơ bản:
        score = 0
        # Tính toán score dựa trên POST data...
        
        # Giả sử điểm qua môn là >= 50
        passed = score >= 50 
        
        # Tạo bản ghi Submission
        submission = Submission.objects.create(score=score, passed=passed)
        
        # Chuyển hướng tới trang kết quả
        return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)
    
    return render(request, 'exam_form.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    context = {
        'course': course,
        'submission': submission,
    }
    return render(request, 'exam_result.html', context)
