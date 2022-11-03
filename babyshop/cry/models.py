from django.db import models



class regform(models.Model):
    fn=models.CharField(max_length=50)
    ln=models.CharField(max_length=50)
    em=models.CharField(max_length=50)
    mn=models.IntegerField()
    pas=models.CharField(max_length=50)
    def __str__(self):
        return self.em
