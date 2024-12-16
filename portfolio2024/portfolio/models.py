from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    # 学生番号　2447000 student_no
    student_no = models.IntegerField(
        verbose_name="学生番号",
        primary_key=True
    )
    # 氏名　下道 俊樹 student_name
    student_name = models.CharField(
        verbose_name="学生氏名",
        max_length=20
    )
    
    USERNAME_FIELD = "student_no"

class System(models.Model):
    student = models.ForeignKey(
        Student,
        verbose_name="学生",
        on_delete=models.CASCADE
    )
    # システム名　ポートフォリオ system_name
    system_name = models.CharField(
        verbose_name="システム名",
        max_length=20
    )
    # システム概要　年間制作作品をまとめたサイト system_summary
    system_summary = models.TextField(
        verbose_name="システム概要"
    )
    # サムネイル画像 system_thumbnail
    system_thumbnail = models.ImageField(
        verbose_name="サムネイル画像",
        upload_to= 'photos'
    )
    # 制作背景　年間制作作品を多くの人に見てもらうため system_background
    system_background = models.TextField(
        verbose_name= "システム背景"
    )