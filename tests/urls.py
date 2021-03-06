from tests.test_app.views import edit_test_wizard_view, new_test_wizard_view

from django.conf.urls import url

urlpatterns = [
    url(r'^wizard/new/(?P<step>.+)/$', new_test_wizard_view, name="test_wizard"),
    url(r'^wizard/edit/(?P<edit_id>\d+)/(?P<step>.+)/$', edit_test_wizard_view, name='test_edit_wizard'),
]
