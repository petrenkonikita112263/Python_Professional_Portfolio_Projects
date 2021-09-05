from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MessageBoardConfig(AppConfig):
    name = "messageboard"


class MessageBoardAdminConfig(AdminConfig):
    default_site = "admin.Comment8orAdminSite"
