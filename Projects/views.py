from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ProjectsFrom
from .models import Projects,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def addComment(request,id):
   project = get_object_or_404(Projects,id=id)

   if request.method =="POST":
      comment_user = request.POST.get("comment_user")
      comment_content = request.POST.get("comment_content")
      newComment = Comment(comment_user = comment_user,comment_content=comment_content)

      newComment.project =project
      newComment.save()

   return redirect(reverse("Projects:detail",kwargs={"id":id}))

def index(request):
   return render(request,"index.html")

def about(request):
   return render(request,"about.html")

@login_required(login_url="User:login")
def dashboard(request):
   projects = Projects.objects.filter(project_user = request.user)
   context={
      "projects":projects
   }
   return render(request,"dashboard.html",context)

@login_required(login_url="User:login")
def addProject(request):
   form = ProjectsFrom(request.POST or None,request.FILES or None)

   if form.is_valid():
      project = form.save(commit=False)
        
      project.project_user = request.user
      project.save()
      messages.success(request,"Proje Başarıyla Oluşturuldu")
      return redirect("Projects:dashboard")
   return render(request,"addProject.html",{"form":form})

@login_required(login_url="User:login")
def updateProject(request,id):
   project = get_object_or_404(Projects,id=id)
   form = ProjectsFrom(request.POST or None,request.FILES or None,instance=project)
   if form.is_valid():
      project=form.save(commit=False)
      project.project_user=request.user
      project.save()
      messages.success(request,"Proje Başarıyla Güncellenmiştir.")
      return redirect("Projects:dashboard")
   return render(request,"update.html",{"form":form})

@login_required(login_url="User:login")
def deleteProject (request,id):
   project = get_object_or_404(Projects,id=id)
   project.delete()
   messages.success(request,"Proje Başarı İle Silindi.")
   return redirect("Projects:dashboard")
   

def detail(request,id):
   #project = Projects.objects.filter(id=id).first()
   project = get_object_or_404(Projects,id=id)

   comments = project.comments.all()
   return render(request,"detail.html",{"project":project,"comments":comments})

def projects(request):
   keyword = request.GET.get("keyword")
   if keyword:
      projects=Projects.objects.filter(project_name__contains=keyword)
      return render(request,"projects.html",{"projects":projects})
   projects = Projects.objects.all()
   return render(request,"projects.html",{"projects":projects})

