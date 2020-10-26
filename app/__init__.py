import quart
import hypercorn
import os
import asyncio
from .utils import blueprints

app = quart.Quart(__name__)
app.config["SECRET_KEY"] = os.urandom(32)
asyncio.ensure_future(blueprints.register_blueprints(app))
