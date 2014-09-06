from django.db import models


class TestMod(models.Model):
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question