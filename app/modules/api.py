import quart
import datetime
from app import config

blueprint = quart.Blueprint("api", __name__)


async def calc_exam_timestamp() -> float:
    tzinfo = datetime.timezone(datetime.timedelta(hours=config.TIMEDELTA))
    curr_datetime = datetime.datetime.now(tz=tzinfo)
    curr_year = curr_datetime.year
    if curr_datetime > datetime.datetime(curr_year,
                                         config.EXAM_MONTH,
                                         config.EXAM_DAY,
                                         config.EXAM_HOUR,
                                         config.EXAM_MIN,
                                         tzinfo=tzinfo):
        exam_datetime = datetime.datetime(curr_year + 1,
                                          config.EXAM_MONTH,
                                          config.EXAM_DAY,
                                          config.EXAM_HOUR,
                                          config.EXAM_MIN,
                                          tzinfo=tzinfo)
    else:
        exam_datetime = datetime.datetime(curr_year,
                                          config.EXAM_MONTH,
                                          config.EXAM_DAY,
                                          config.EXAM_HOUR,
                                          config.EXAM_MIN,
                                          tzinfo=tzinfo)
    return exam_datetime.timestamp()


@blueprint.route("/api/timestamp")
async def get_time():
    timestamp = await calc_exam_timestamp()
    json = {"timestamp": timestamp}
    return quart.jsonify(json)
