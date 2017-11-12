from django.db import models

class poll (models.Model):
    title = models.CharField(max_length = 12)
    text = models.CharField(max_length  = 50)
    def __str__(self):
        return self.title
    
class choice(models.Model):
    under = models.ForeignKey(poll, on_delete = models.CASCADE)
    text = models.CharField(max_length- 30)
    fame = models.PositiveIntegerField()
    def __str__(self):
        return self.text+' - '+str(fame)

    