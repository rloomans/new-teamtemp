import cspreports.urls
from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin as djadmin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.static import serve as serve_static
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


from teamtemp.views import TeamResponseHistoryViewSet, TeamTemperatureViewSet, TeamsViewSet, TemperatureResponseViewSet, \
    UserViewSet, WordCloudImageViewSet, admin_view, bvc_view, cron_view, health_check_view, home_view, \
    media_view, reset_view, robots_txt_view, set_view, submit_view, team_view, user_view, wordcloud_view, login_view, \
    super_view

router = routers.DefaultRouter()
router.register(r'word_cloud_images', WordCloudImageViewSet)
router.register(r'users', UserViewSet)
router.register(r'team_temperatures', TeamTemperatureViewSet)
router.register(r'temperature_responses', TemperatureResponseViewSet)
router.register(r'team_response_histories', TeamResponseHistoryViewSet)
router.register(r'teams', TeamsViewSet)

urlpatterns = [
    re_path(r'^cs$', home_view, {'survey_type': 'CUSTOMERFEEDBACK'}),
    re_path(r'^drs$', home_view, {'survey_type': 'DEPT-REGION-SITE'}),
    re_path(r'^$', home_view, name='home'),
    re_path(r'^about$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    re_path(r'^user/?$', user_view, name='user'),
    re_path(r'^super/(?P<survey_id>[0-9a-zA-Z]{8})/?$', super_view, name='super'),
    re_path(r'^admin/(?P<survey_id>[0-9a-zA-Z]{8})/?$', admin_view, name='admin'),
    re_path(r'^login/(?P<survey_id>[0-9a-zA-Z]{8})/?$', login_view, name='login'),
    re_path(r'^login/(?P<survey_id>[0-9a-zA-Z]{8})(?P<redirect_to>/.+)$', login_view, name='login'),
    re_path(r'^set/(?P<survey_id>[0-9a-zA-Z]{8})/?$', set_view, name='set'),
    re_path(r'^admin/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})/?$', admin_view, name='admin'),
    re_path(r'^(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})$', submit_view, name='submit'),

    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/?$', bvc_view, name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/i(?P<num_iterations>[0-9]{1,3})$', bvc_view, name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})/i(?P<num_iterations>[0-9]{1,3})$', bvc_view,
        name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/?$', bvc_view, name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})/?$', bvc_view, name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})/(?P<archive_id>[0-9]{1,20})/?$', bvc_view,
        name='bvc'),

    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/region=(?P<region_names>[-\w\,]{1,64})/?$', bvc_view, name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/site=(?P<site_names>[-\w\,]{1,64})/?$', bvc_view, name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/dept=(?P<dept_names>[-\w\,]{1,64})/?$', bvc_view, name='bvc'),

    re_path(
        r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/dept=(?P<dept_names>[-\w\,]{0,64})/region=(?P<region_names>[-\w\,]{0,64})/site=(?P<site_names>[-\w\,]{0,64})$',
        bvc_view, name='bvc'),
    re_path(
        r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/dept=(?P<dept_names>[-\w\,]{0,64})/region=(?P<region_names>[-\w\,]{0,64})/site=(?P<site_names>[-\w\,]{0,64})$',
        bvc_view, name='bvc'),

    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/region=(?P<region_name>[-\w\,]{1,64})/?$',
        bvc_view,
        name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/site=(?P<site_name>[-\w\,]{1,64})/?$', bvc_view,
        name='bvc'),
    re_path(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})/dept=(?P<dept_name>[-\w\,]{1,64})/?$', bvc_view,
        name='bvc'),

    re_path(r'^reset/(?P<survey_id>[0-9a-zA-Z]{8})/?$', reset_view, name='reset'),
    re_path(r'^cron/(?P<pin>.{4,100})$', cron_view, name='cron'),
    re_path(r'^team/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>[-\w]{1,64})$', team_view, name='team'),
    re_path(r'^team/(?P<survey_id>[0-9a-zA-Z]{8})/?$', team_view, name='team'),
    re_path(r'^wordcloud/(?P<word_hash>[a-f0-9]{40})?$', wordcloud_view, name='wordcloud'),
    re_path(r'^static/(.*)$', serve_static, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(.*)$', media_view, {'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path(r'^healthcheck/?$', health_check_view, name='healthcheck'),
    re_path(r'^robots\.txt', robots_txt_view, name='robots_txt'),
    re_path(r'^favicon\.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')), name='favicon'),
    re_path(r'^djadmin/', djadmin.site.urls),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^docs/', include_docs_urls(title='Team Temperature API')),
    re_path(r'^csp/', include('cspreports.urls')),
]
