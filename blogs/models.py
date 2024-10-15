from django.db import models
import uuid
# Create your models here.



class BlogModel(models.Model):
    blog_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    content = models.TextField(max_length= 400)
    private = models.BooleanField(default=False)
    data_created = models.DateTimeField(auto_now_add=True)