from django.contrib import admin

# Register your models here.
# 모델을 관리자페이지에 등록해서 다루고 싶을 때
# 관리자페이지의 화면을 커스터마이징 하고싶을때

from .models import Bookmark
admin.site.register(Bookmark)