from django.urls import path

from . import views


app_name = 'kalenteri'
urlpatterns = [
      path('', views.index, name="index"),
      path("kalenteri/", views.KalenteriViewNew.as_view(), name="kalenteri"),
      path("kalenterit/", views.Kalenteriview.as_view(), name="kalenterit"),
      path("ohjelmasi/new", views.creat_ohjelmasi, name="uusi_ohjelma"),
      path("ohjelmasi/edit/<init:pk>/", views.OhjelmasiEdit.as_view(), name="ohjelmasi_edit"),
      path("ohjelmasi/<int:ohjelmasi_id>/details/", views.ohjelmasi_datails, name="ohjelmasi-detail"),
      path(
        "add_ohjelmasi/<int:ohjelma_id>", views.add_ohjelma, name="add_ohjelma"
      ),
      path(
        "ohjelmasi/<int:pk>/remove",
        views.OhjelmasiDeleteView.as_view(),
        name="remove_ohjelmasi",
      ),
      path("all-ohjelmasi_list/", views.AllOhjelmasiListView.as_view(), name="all_ohjelmasi"),
      path(
        "running-ohjelmasi-listt/",
        views.RunningOhjelmasiListView.as_view(),
        name="runnis-ohjelmasi"
      ),    
]







