from django.db import models


# ... create FAQsModel 
class FAQ(models.Model):
    
    # .. stop skipping 
    id = models.AutoField(primary_key=True)
    
    # .. string 
    question = models.CharField(default="", null=True, blank=True, max_length=500)
    answer = models.CharField(default="", null=True, blank=True, max_length=1000)
    
    # .. date fields 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # overide the string method 
    def __str__(self):
        return "Question: {0} => {1}".format(self.id, self.question)
      


    