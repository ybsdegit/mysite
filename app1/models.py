from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增的id列作为主键
    email = models.CharField(max_length=32)  # -> varchar(32)
    pwd = models.CharField(max_length=32)  # -> varchar(32)
    
    def __str__(self):
        return self.email


class Press(models.Model):
    id = models.AutoField(primary_key=True)  # id 主键
    name = models.CharField(max_length=32)  # 出版社名称
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增id
    title = models.CharField(max_length=30)  # 书名
    price = models.IntegerField()  # 价格
    # Django 1.11 默认级联删除， Django2.0 之后必须制定 on_delete
    # to='' 关联的表名
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Author(models.Model):
    """作者表"""
    id = models.AutoField(primary_key=True)  # 自增 id 主键
    name = models.CharField(max_length=32)  # 作者名字
    books = models.ManyToManyField(to='Book')  # ORM 层面建立的一个多对多关系，不是作者表的一个字段
    
    def __str__(self):
        return self.name

# class Author2Book(models.Model):
#     """坐车和书籍的关系表"""
#     id = models.AutoField(primary_key=True)
#     author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
#     book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
