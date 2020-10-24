from app import app
from app.modules import index


async def register_blueprints():
    app.register_blueprint(index.blueprint)

