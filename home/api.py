from flask.views import MethodView

class HomeAPI(MethodView):
    def __init__(self):
        pass

    def get(self):
        return "Home Page"

class DashboardAPI(MethodView):
   
    def __init__(self):
        pass

    def get(self):
        return "Dashboard"
