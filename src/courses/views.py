from django.shortcuts import render, get_object_or_404, redirect
from django.views import View 
from .models import Course
from .forms import CourseModelForm 

# BASE VIEW Class = VIEW
class CourseUpdateView(View):
    template_name = 'courses/course_update.html'
    def get_object(self): #overwrite your detail view
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *arg, **kwargs): #id=None: id is not requiered
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *arg, **kwargs): #id=None: id is not requiered
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = CourseModelForm()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class CourseDeleteView(View):
    template_name = 'courses/course_delete.html'
    def get_object(self): #overwrite your detail view
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *arg, **kwargs): #id=None: id is not requiered
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, *arg, **kwargs): #id=None: id is not requiered
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *arg, **kwargs): #id=None: id is not requiered
        form = CourseModelForm()
        context = {'form': form} #because template use form parameter
        return render(request, self.template_name, context)

    def post(self, request, *arg, **kwargs): #id=None: id is not requiered
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm() #rerender let the form be clean
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

# #inheritance property
# class MyListView(CourseListView):
#     queryset = Course.objects.filter(id=1)

class CourseView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *arg, **kwargs): #id=None: id is not requiered
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        print(context)
        return render(request, self.template_name, context)

# class CourseView(View):
#     # GET method
#     template_name = 'about.html'
#     def get(self, request, *arg, **kwargs):
#         return render(request, self.template_name, {})

# Create your views here.
# HTTP methods
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
   