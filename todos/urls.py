from django.urls import path
from . import views
urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('', views.hello_python_view, name='hello_python'),
    path('htmlrender', views.hello_html_view, name='hello_html'),
    path('special', views.special_view, name='special'),
    path('helloname/<str:name>', views.hello_path, name='hello_path'),
    path('add/<int:num1>/<int:num2>', views.hello_add, name='hello_add'),
    path('multiply/<int:num1>/<int:num2>', views.hello_multiply, name='hello_multiply'),
    path('helloquery', views.hello_query, name='hello_query'),
    path('postendpoint', views.post_example, name='post_example'),
    path('submitendpoint', views.submit_example, name='submit_example'),
    path('submitdjango', views.submit_django_form, name='submit_django'),
    path('templating', views.template_view, name='templating'),
    path('todos', views.todos_view, name='todos'),
    path('person/<int:person_id>', views.person_details, name='person_details'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('toggle_todo/<int:todo_id>', views.toggle_todo_done, name='toggle_todo'),



]