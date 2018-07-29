from flask import Blueprint
from home.api import HomeAPI, DashboardAPI

home_app = Blueprint('home_app', __name__)

home_view = HomeAPI.as_view('home_api')
home_app.add_url_rule('/home', view_func=home_view, methods=['GET',])

dashboard_view = DashboardAPI.as_view('dashboard_api')
home_app.add_url_rule('/dashboard', view_func=dashboard_view, methods=['GET',])