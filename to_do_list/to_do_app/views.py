from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from to_do_app.models import Task, Comment, Tag
from to_do_app.forms import TaskForm, CommentForm, TagForm
# Create your views here.

class HomeView(View):
  def get(self, request):
    
    
    tasks = Task.objects.all()
    task_form = TaskForm()
    

    html_data = {
      'task_list' : tasks, 
      'form' : task_form
    }
    
    return render(
      request = request,
      template_name = 'index.html',
      context = html_data,
        )


  def post(self, request):
    
    task_form = TaskForm(request.POST)
    task_form.save()

    return redirect('home')

    

class TaskDetailView(View):
  def get(self, request, task_id):
    task = Task.objects.get(id=task_id)
    # this is saying that we want to create a variable to hold a specific task id, we want to get the task id of the task we click on on the Home page the id = task_id from the variable we sent in the url
    

    task_form = TaskForm(instance=task)
    # instance = do this to this specific task

    comments = Comment.objects.filter(task = task)# task is already holding the id info
    comment_form = CommentForm(task_object=task)

    tag = Tag.objects.all()
    tag_form = TagForm()

    html_data = {
      'task_object' : task, 
      'form' : task_form,
      'comment_list' : comments, #'variable" uses in html
      'comment_form' : comment_form,
      'tag_list' : tag,
      'tag_form' : tag_form

    }
    
    return render(
      request = request,
      template_name = 'detail.html',
      context = html_data
    )



  def post(self, request, task_id):
    task = Task.objects.get(id=task_id)

    if 'update' in request.POST:
      task_form = TaskForm(request.POST, instance=task)
      task_form.save()
    elif 'delete' in request.POST:
      task.delete()
    elif 'add' in request.POST:
      comment_form = CommentForm(request.POST, task_object=task)
      comment_form.save()
      return redirect('task_detail', task.id)
    elif 'create' in request.POST:
      tag_form = TagForm(request.POST)
      tag_form.save()
      return redirect('task_detail', task.id)

    return redirect('home')
   

