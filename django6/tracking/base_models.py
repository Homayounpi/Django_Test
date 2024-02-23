from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class BaseAPIRequestLog(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)

    username_persistent = models.CharField(max_length=getattr(settings,'DRF_TRACKING_USERNAME_LENGTH',200),blank=True,null=True)
    requested_at = models.DateTimeField(db_index=True)
    response_ms = models.PositiveIntegerField(default=0)
    path = models.CharField(max_length=getattr(settings,"DRF_TRACKING_PATH_LENGTH",200),db_index=True,help_text='url path')
    view = models.CharField(max_length=getattr(settings,"DRF_TRACKING_VIEW_LENGTH",200),blank=True,null=True,db_index=True,help_text='method called by this endpoint')
    view_method = models.CharField(max_length=getattr(settings,'DRF_TRACKING_VIEW_METHOD_LENGTH',200),blank=True,null=True,db_index=True)
    remote_addr = models.GenericIPAddressField()
    host = models.URLField()
    method = models.CharField(max_length=10)
    query_params = models.TextField(blank=True,null=True)
    data = models.TextField(blank=True,null=True)
    response = models.TextField(blank=True,null=True)
    errors = models.TextField(blank=True,null=True)
    status_code = models.PositiveIntegerField(blank=True,null=True,db_index=True)

    class Meta:
        abstract =True
        verbose_name = 'API Request Lg' 
    def __str__(self) :
        return f'{self.method}  {self.path}'