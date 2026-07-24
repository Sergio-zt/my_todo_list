from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from todolist.models import Task, Tag
from todolist.forms import TaskForm
from django.views import View


class TaskListView(generic.ListView):
    model = Task
    template_name = "todolist/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").order_by("is_done", "-created_at")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm  # Используем кастомную форму
    success_url = reverse_lazy('todolist:task-list')

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm  # Используем кастомную форму
    success_url = reverse_lazy('todolist:task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:task-list")



class TaskToggleStatusView(View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todolist:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todolist/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todolist:tag-list")

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todolist:tag-list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist:tag-list")
