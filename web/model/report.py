from django.db import models
from web.model.case import Case


class Report(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    user_id=models.IntegerField(blank=False)
    post_id=models.IntegerField(blank=False)
    case_name=models.CharField(max_length=64)
    browser=models.CharField(max_length=32)
    resolution=models.CharField(max_length=32)
    browser_size=models.CharField(max_length=32)
    result=models.IntegerField()
    result_content=models.TextField(max_length=1024)
    ext=models.TextField(max_length=1024)

    def __unicode__(self):
        return "%d:%s" % (self.id, self.case.name)
