from django.db import models


class Line(models.Model):
    name = models.CharField(verbose_name='线路名', max_length=50)

    def __str__(self):
        return self.name


class Train(models.Model):
    line = models.ForeignKey(Line, related_name='trains', on_delete=models.CASCADE)
    number = models.CharField(verbose_name='车体号', max_length=50)

    def __str__(self):
        return self.number


class CleanRecords(models.Model):
    train = models.ForeignKey(Train, related_name='records', on_delete=models.CASCADE)
    clean_front = models.BooleanField(verbose_name='是否端洗', default=True)
    clean_date = models.DateTimeField(verbose_name='清洗日期', auto_now=True)

    def __str__(self):
        return "#".join((self.train.number, str(self.clean_front), self.clean_date.strftime("%Y-%m-%d")))
