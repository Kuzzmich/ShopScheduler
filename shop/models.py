from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField(max_length=200, verbose_name='Shop name')
    shop_owner_id = models.ForeignKey(User,
                                      related_name='shop',
                                      on_delete=models.CASCADE,
                                      verbose_name='Shop owner id')
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.CharField(max_length=200, verbose_name='Schedule name')
    shop_id = models.OneToOneField(Shop,
                                   related_name='schedule',
                                   on_delete=models.CASCADE,
                                   verbose_name='Schedule owner')


class DayOfWeek(models.Model):
    name = models.CharField(max_length=10, verbose_name='Day of week name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Days of week name'


class ScheduleRecord(models.Model):
    schedule_id = models.ForeignKey(Schedule,
                                    related_name='schedule_records',
                                    on_delete=models.CASCADE,
                                    verbose_name='Schedule')
    day_of_week_id = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE, verbose_name='Day of week')
    time_open = models.TimeField(verbose_name='Opening time', blank=True, null=True)
    time_close = models.TimeField(verbose_name='Closing time', blank=True, null=True)
    is_holiday = models.BooleanField(verbose_name='Is holiday', default=True)

    class Meta:
        ordering = ['day_of_week_id']


class Break(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    schedule_record_id = models.ForeignKey(ScheduleRecord,
                                           related_name='breaks',
                                           on_delete=models.CASCADE,
                                           verbose_name='Schedule record')
    time_start = models.TimeField(verbose_name='Start time')
    time_end = models.TimeField(verbose_name='End time')

    class Meta:
        ordering = ['time_start']
