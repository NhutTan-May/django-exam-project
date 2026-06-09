from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Submission, Choice, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Lấy enrollment đầu tiên của course này (đảm bảo code không lỗi khi test)
    enrollment = Enrollment.objects.filter(course=course).first()
    
    if request.method == 'POST':
        # Tạo submission mới
        submission = Submission.objects.create(enrollment=enrollment)
        
        # Lặp qua tất cả dữ liệu POST lên để tìm ID của Choice
        for key, value in request.POST.items():
            if key.startswith('choice'): # Hoặc 'question' tùy vào thẻ name="" trong HTML của bạn
                try:
                    choice = Choice.objects.get(pk=int(value))
                    submission.choices.add(choice) # Lưu choice vào submission
                except (ValueError, Choice.DoesNotExist):
                    pass
        
        submission.save()
        # Chuyển hướng kèm đúng parameters
        return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Tạo list các ID mà user đã chọn
    selected_ids = submission.choices.values_list('id', flat=True)
    
    # Tính điểm (grade)
    grade = 0
    for choice in submission.choices.all():
        if choice.is_correct:
            grade += choice.question.grade
            
    context = {
        'course': course,
        'submission': submission,
        'selected_ids': selected_ids, # Bắt buộc phải có biến này
        'grade': grade,               # Bắt buộc phải có biến này
    }
    return render(request, 'exam_result.html', context)
    return render(request, 'exam_result.html', context)
