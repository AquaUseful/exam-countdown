from app.modules import index, api


async def register_blueprints(app):
    app.register_blueprint(index.blueprint)
    app.register_blueprint(api.blueprint)
