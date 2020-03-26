from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Projects(models.Model):

    project_user = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Kullanıcı")
    project_name=models.CharField(max_length=50, verbose_name="Proje Adı")
    project_content = RichTextField()
    project_created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi") 
    project_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    
    def __str__(self):
        return self.project_name

    class  Meta:
        ordering =['-project_created_date']
class Comment(models.Model):
    project = models.ForeignKey(Projects,on_delete=models.CASCADE,verbose_name="Proje",related_name="comments")
    comment_user=models.CharField(max_length=50,verbose_name="İsim")
    comment_content= models.CharField(max_length=200,verbose_name="Yorum")
    comment_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment_user
    class  Meta:
        ordering =['-comment_date']