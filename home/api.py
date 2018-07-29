from flask.views import MethodView
from registration.decorators import app_required

class HomeAPI(MethodView):
    def __init__(self):
        pass

    def get(self):
        return "Home Page"

class DashboardAPI(MethodView):
   
    def __init__(self):
        pass

    @app_required
    def get(self):
        return "Dashboard"
