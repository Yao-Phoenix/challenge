from web.config import configs
from flask import Blueprint, Flask, render_template

def register_blueprints(app):
    from web.handlers import job, house
    app.register_blueprint(job)
    app.register_blueprint(house)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_blueprints(app)
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404
    return app

if __name__ == '__main__':
    app.run()
