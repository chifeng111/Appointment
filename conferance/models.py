from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):
    user = models.OneToOneField(User)      #这里的user与User是一对一的关系
    phone = models.CharField(max_length=11)#字符型，必须有个参数max_length字符最大值
    def __str__(self):
        return self.user.username   #返回的对象为username


#会议室模型
class ConfeRoom(models.Model):
    num = models.CharField(max_length=5)
    size = models.CharField(max_length=5)
    class MEAT:                 #引入MEAT中间件，为了在前端显示的时候以“num”顺序排列，与下一个类似
        ordering = ["num"]
    def __str__(self):
        return self.num


#订单信息
class Order(models.Model):
    user = models.ForeignKey(MyUser, default=1)
    room = models.ForeignKey(ConfeRoom, default=1)
    time = models.DateField()

    def __str__(self):
        return str(self.user)