from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
class Todoapp(models.Model):

    title = models.CharField(max_length=255,blank=True)
    description = RichTextField()
    is_done = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.id)])
    


    
