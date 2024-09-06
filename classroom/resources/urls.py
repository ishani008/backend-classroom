from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher', views.teacher_index, name="teacher"),
    path('profileT', views.profileT, name='profileT'),
    path('displayData', views.displayData, name='displayData'),
    path('updatingData', views.updatingData, name='updatingData'),
    path('addCourseSubject', views.addCourseSubject, name='addCourseSubject'),
    path('addCourse', views.addCourse, name='addCourse'),
    path('allCourses', views.allCourses, name='allCourses'),
    path('formUploadC', views.formUploadC, name='formUploadC'),
    path('addingCourse', views.addingCourse, name='addingCourse'),
    path('deleteCourse', views.deleteCourse, name='deleteCourse'),
    path('displayCourseDetails', views.displayCourseDetails,
         name='displayCourseDetails'),
    path('formUploadTD', views.formUploadTD, name='formUploadTD'),
    path('addingTD', views.addingTD, name='addingTD'),
    path('formUploadTP', views.formUploadTP, name='formUploadTP'),
    path('addingTP', views.addingTP, name='addingTP'),
    path('formUploadCorre', views.formUploadCorre, name='formUploadCorre'),
    path('addingCorr', views.addingCorr, name='addingCorr'),
    path('deleteCourseFile', views.deleteCourseFile, name='deleteCourseFile'),
    path('deleteTD', views.deleteTD, name='deleteTD'),
    path('deleteTP', views.deleteTP, name='deleteTP'),
    path('deleteCorr', views.deleteCorr, name='deleteCorr'),
    path('formUploadHW', views.formUploadHW, name='formUploadHW'),
    path('sendingHW', views.sendingHW, name='sendingHW'),
    path('displayAllStudents', views.displayAllStudents, name='displayAllStudents'),
    path('statistics', views.statistics, name='statistics'),
    path('student', views.student_index, name='student'),
    path('student/course', views.student_course, name='student_course'),
    path('student/join_course', views.student_join_course,
         name='student_join_course'),
    path('student/to_do', views.student_to_do, name='student_to_do'),
    path('student/profile', views.student_profile, name='student_profile'),
    path('student/edit_picture', views.student_picture, name='student_picture'),
    path('student/put_todo', views.student_put_todo, name='student_put_todo'),
    path('student/edit_profile', views.student_edit_profile,
         name='student_edit_profile'),
    path('student/delete_course', views.destroy,
         name='destroy'),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name='logout'),
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),

]
