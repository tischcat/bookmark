from django.urls import path
# url - 주소(정규표현식으로 주소를 표현), 뷰
# path - 주소(기존 정규표현식을 간단히 표현할수 있게 컨버터), 뷰
# re_path - 주소(정규표현식으로 주소를 표현), 뷰

# 뷰는 함수형, 클래스형 뷰로 나눠짐
# 결국 장고에서 모든뷰는 함수형으로 동작하게 되어있다. (클래스형뷰는 .as_view 로 함수형으로 만들어줌)
from .views import BookmarkList, BookmarkCreate, BookmarkUpdate, BookmarkDelete

urlpatterns = [
    # urlpatterns 안에 path 쓰는법
    # 함수형뷰: 함수이름
    # 클래스형뷰: 클래스이름.as_view
    # 글번호 받는방법
    # 1. naver.com/blog/update/?doc_id=1234 (예전방식)
    # 2. naver.com/blog/update/1234/ (주소체계 자체에 집어넣음)
    path("delete/<int:pk>/", BookmarkDelete.as_view(), name='bookmark_delete'),
    path("update/<int:pk>/", BookmarkUpdate.as_view(), name='bookmark_update'),
    path("write/", BookmarkCreate.as_view(), name='bookmark_create'),
    path("", BookmarkList.as_view() , name='bookmark_list'),
]