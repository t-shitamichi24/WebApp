from django.forms import ModelForm
from .models import Student

class PhotoPostForm(ModelForm):
    class Meta:
        # モデルのクラス
        model = PhotoPost
        # フォームで使用するモデルのフィールドを指定
        fields = ['category', 'title', 'comment', 'image1', 'image2']