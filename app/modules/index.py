import quart

blueprint = quart.Blueprint("index", __name__)


@blueprint.route("/")
async def root():
    return quart.redirect("/index")

@blueprint.route("/index")
async def index():
    return await quart.render_template("index.html", title="Countdown")