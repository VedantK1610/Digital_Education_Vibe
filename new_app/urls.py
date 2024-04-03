from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/", views.courses, name="courses"),
    path("ft-courses/", views.ft_courses, name="ft-courses"),
    path("aboutus/", views.about_us, name="about-us"),
    path("courses/BCA", views.bca_course, name="bca_course"),
    path("courses/BCOM", views.bcom_course, name="bcom_course"),
    path("courses/BA", views.ba_course, name="ba_course"),
    path("courses/MCOM", views.mcom_course, name="mcom_course"),
    path("courses/BBA", views.bba_course, name="bba_course"),
    path("courses/MCA", views.mca_course, name="mca_course"),
    path("courses/MBA-courses", views.mba_courses, name="mba_course"),
    path("FT_courses/data-science", views.data_science, name="data_science"),
]