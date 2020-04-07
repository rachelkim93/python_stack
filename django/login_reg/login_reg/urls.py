"""login_reg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.logreg.urls')),
]


"""
1. Show the user the login/registration page
2. Submit the form (registration)
    2a. Validate
    2b. Check if they're already registered
    2c. Hash the password
    2d. Save the user to the db
    2e. (Log the user in)
3. Submit the form (login)
    3a. Validate
    3b. Check if they've registered
    3c. Hash & Check the password
    3d. Log the user in (session)

"""