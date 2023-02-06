from django.test import TestCase
from .models import User
# test 작성시 참고 링크1(arrayfield test): https://velog.io/@heka1024/Django-ArrayField-%EC%9A%B0%EC%95%84%ED%95%98%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
# test 작성시 참고 링크2: https://www.coninggu.com/8


# class UserTest(TestCase):
#     def test_input_tag_at_create(self):
#         # 생성시에 태그를 넣을 수 있다
#         user = User.objects.create(
#             username="seokyoung",
#             nickname="sgaeng",


#             title="title",
#             content="content",
#             user_hastTags=["python", "django", "notion"],
#         )

#         assert User.objects.count() == 1
# 		assert User.user_hastTags == ["python", "django", "notion"]


#     def test_tag_filter(self):
#         # 태그로 필터링 할 수 있다
#         User.objects.create(
#             title="title",
#             content="content",
#             user_hastTags=["python", "django", "notion"],
#         )
#         User.objects.create(
#             title="title",
#             content="content",
#             user_hastTags=["python", "django"],
#         )
#         User.objects.create(
#             title="title",
#             content="content",
#             user_hastTags=["python"],
#         )

#         assert User.objects.count() == 3
# 		assert User.objects.filter(tags__contains=["python"]).count() == 3
# 		assert User.objects.filter(tags__contains=["django"]).count() == 2
# 		assert User.objects.filter(tags__contains=["notion"]).count() == 1

#     def test_tag_length(self):
#         # 태그의 길이를 알 수 있다
#         User.objects.create(title="title", content="content", tags=["a", "b", "c"])
#         User.objects.create(title="title", content="content", tags=["a", "b"])
#         User.objects.create(title="title", content="content", tags=["a", "c"])
#         Post.objects.create(title="title", content="content", tags=["a"])

#         qs = Post.objects.filter(tags__len=2)

#         assert qs.count() == 2
