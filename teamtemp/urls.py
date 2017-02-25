import cspreports.urls
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin as djadmin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.static import serve as serve_static
from rest_framework import routers

from teamtemp.views import TeamResponseHistoryViewSet, TeamTemperatureViewSet, TeamsViewSet, TemperatureResponseViewSet, \
    UserViewSet, WordCloudImageViewSet, admin_view, bvc_view, cron_view, health_check_view, home_view, \
    media_view, reset_view, robots_txt_view, set_view, submit_view, team_view, user_view, wordcloud_view, login_view

router = routers.DefaultRouter()
router.register(r'word_cloud_images', WordCloudImageViewSet)
router.register(r'users', UserViewSet)
router.register(r'team_temperatures', TeamTemperatureViewSet)
router.register(r'temperature_responses', TemperatureResponseViewSet)
router.register(r'team_response_histories', TeamResponseHistoryViewSet)
router.register(r'teams', TeamsViewSet)

urlpatterns = [
    url(r'^cs$', home_view, {'survey_type': 'CUSTOMERFEEDBACK'}),
    url(r'^drs$', home_view, {'survey_type': 'DEPT-REGION-SITE'}),
    url(r'^$', home_view, name='home'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^user/?$', user_view, name='user'),
    url(r'^admin/(?P<survey_id>[0-9a-zA-Z]{8})/?$', admin_view, name='admin'),
    url(r'^login/(?P<survey_id>[0-9a-zA-Z]{8})/?$', login_view, name='login'),
    url(r'^login/(?P<survey_id>[0-9a-zA-Z]{8})(?P<redirect_to>/.+)$', login_view, name='login'),
    url(r'^set/(?P<survey_id>[0-9a-zA-Z]{8})/?$', set_view, name='set'),
    url(r'^admin/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})/?$', admin_view, name='admin'),
    url(r'^(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})$', submit_view, name='submit'),

    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/?$', bvc_view, name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/i(?P<num_iterations>[0-9]{1,3})$', bvc_view, name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})/i(?P<num_iterations>[0-9]{1,3})$', bvc_view,
        name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/?$', bvc_view, name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})/?$', bvc_view, name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})/(?P<archive_id>[0-9]{1,20})/?$', bvc_view,
        name='bvc'),

    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/region=(?P<region_names>[-\w\,]{1,64})/?$', bvc_view, name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/site=(?P<site_names>[-\w\,]{1,64})/?$', bvc_view, name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/dept=(?P<dept_names>[-\w\,]{1,64})/?$', bvc_view, name='bvc'),

    url(
        r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/dept=(?P<dept_names>[-\w\,]{0,64})/region=(?P<region_names>[-\w\,]{0,64})/site=(?P<site_names>[-\w\,]{0,64})$',
        bvc_view, name='bvc'),
    url(
        r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/dept=(?P<dept_names>[-\w\,]{0,64})/region=(?P<region_names>[-\w\,]{0,64})/site=(?P<site_names>[-\w\,]{0,64})$',
        bvc_view, name='bvc'),

    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/region=(?P<region_name>[-\w\,]{1,64})/?$',
        bvc_view,
        name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/site=(?P<site_name>[-\w\,]{1,64})/?$', bvc_view,
        name='bvc'),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/dept=(?P<dept_name>[-\w\,]{1,64})/?$', bvc_view,
        name='bvc'),

    url(r'^reset/(?P<survey_id>[0-9a-zA-Z]{8})/?$', reset_view, name='reset'),
    url(r'^cron/(?P<pin>[0-9]{4,16})$', cron_view, name='cron'),
    url(r'^team/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})$', team_view, name='team'),
    url(r'^team/(?P<survey_id>[0-9a-zA-Z]{8})/?$', team_view, name='team'),
    url(r'^wordcloud/(?P<word_hash>[a-f0-9]{40})?$', wordcloud_view, name='wordcloud'),
    url(r'^static/(.*)$', serve_static, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^media/(.*)$', media_view, {'document_root': settings.MEDIA_ROOT}, name='media'),
    url(r'^healthcheck/?$', health_check_view, name='healthcheck'),
    url(r'^robots\.txt', robots_txt_view, name='robots_txt'),
    url(r'^favicon\.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')), name='favicon'),
    url(r'^djadmin/', include(djadmin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^csp/', include(cspreports.urls)),
]
