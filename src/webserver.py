from flask import Flask
from src.outlet import Outlet

def create_webserver(outlet: Outlet) -> Flask:
    app = Flask(__name__)

    @app.get('/')
    def index():
        return app.send_static_file("index.html")

    @app.post('/toggle/')
    def toggle():
        outlet.toggle()
        # return code 204 to tell browser not to navigate to this page
        return ('', 204)

    return app
