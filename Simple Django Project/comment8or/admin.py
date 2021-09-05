from django.contrib import admin


class Comment8orAdminSite(admin.AdminSite):
    """Custom admin site for Comment8or application."""
    title_header = "c8 site admin"
    site_header = "Comment8or administration"
    index_title = "Comment8or site admin"
    logout_template = "comment8or/logged_out.html"
