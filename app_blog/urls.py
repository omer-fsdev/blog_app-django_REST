
from rest_framework import routers
from .views import(
    BlogCategoryView,
    BlogPostView,
    BlogCommentView,
)
router = routers.DefaultRouter()
router.register('categories', BlogCategoryView)
router.register('posts', BlogPostView)
router.register('comments', BlogCommentView)

# urlpatterns = [
#    # path('blog/', ),
# ]

# if we have only routers:
urlpatterns = router.urls
