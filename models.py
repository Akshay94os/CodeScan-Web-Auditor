from django.db import models

class CodeScan(models.Model):
    title = models.CharField(max_length=150)
    source_code = models.TextField()
    detected_errors = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default="Analyzed")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
