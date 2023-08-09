from crud_operation.viewsets import MemberViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('member',MemberViewsets)