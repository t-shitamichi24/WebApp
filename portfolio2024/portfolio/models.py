from django.db import models
from django.contrib.auth.models import AbstractUser

def user_path(instance, filename):
    return f'photos/{instance.student.student_no}'

# Create your models here.
class Student(AbstractUser):
    # 学生番号　2447000 student_no
    student_no = models.IntegerField(
        verbose_name="学生番号",
        primary_key=True
    )
    # 氏名　下道 俊樹 student_name
    username = models.CharField(
        verbose_name="学生氏名",
        max_length=20,
        blank=True
    )
    
    USERNAME_FIELD = "student_no"
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username

class System(models.Model):
    student = models.OneToOneField(
        Student,
        verbose_name="学生",
        on_delete=models.CASCADE,
        primary_key=True
    )
    # システム名　ポートフォリオ system_name
    system_name = models.CharField(
        verbose_name="システム名",
        max_length=20,
        blank=True,
        null=True
    )
    # システム概要　年間制作作品をまとめたサイト system_summary
    system_summary = models.TextField(
        verbose_name="システム概要",
        blank=True,
        null=True
    )
    # システムURL
    system_url = models.URLField(
        verbose_name="システムURL",
        blank=True,
        null=True
    )
    # サムネイル画像 system_thumbnail
    system_thumbnail = models.ImageField(
        verbose_name="サムネイル画像",
        upload_to= user_path,
        blank=True,
        null=True
    )
    # 制作背景　年間制作作品を多くの人に見てもらうため system_background
    system_background = models.TextField(
        verbose_name= "システム背景",
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.student)