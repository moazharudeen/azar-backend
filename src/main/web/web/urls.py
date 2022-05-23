"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core import views
from core.customer import views as customer_views
from core.courier import views as courier_views, apis as courier_apis

customer_urlpatters = [
    path('', customer_views.customer_page, name="home"),
    path('profile/', customer_views.profile_page, name="profile"),
    path('payment_method/', customer_views.payment_method_page, name="payment_method"),
    path('create_job/', customer_views.create_job_page, name="create_job"),
    path('jobs/current/', customer_views.current_jobs_page, name="current_jobs"),
    path('jobs/archived/', customer_views.archived_jobs_page, name="archived_jobs"),
    path('jobs/<job_id>/', customer_views.job_page, name="job"),

]

courier_urlpatters = [
    path('', courier_views.courier_page, name="home"),
    path('jobs/available/', courier_views.available_jobs_page, name="available_jobs"),

    path('api/jobs/available/', courier_apis.available_jobs_api, name="available_jobs_api"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('accounts/', include('allauth.urls')),

    path('', views.home),

    path('customer/', include((customer_urlpatters, 'customer'))),
    path('courier/', include((courier_urlpatters, 'courier'))),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)