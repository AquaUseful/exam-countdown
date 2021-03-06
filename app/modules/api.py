import quart
import datetime
import os
try:
    from app import config
except ImportError:
    pass

blueprint = quart.Blueprint("api", __name__)


async def calc_exam_timestamp() -> float:
    try:
        exam_month = config.EXAM_MONTH
        exam_day = config.EXAM_DAY
        exam_hour = config.EXAM_HOUR
        exam_min = config.EXAM_MIN
        timedelta = config.TIMEDELTA
    except NameError:
        exam_month = int(os.environ["EXAM_MONTH"])
        exam_day = int(os.environ["EXAM_DAY"])
        exam_hour = int(os.environ["EXAM_HOUR"])
        exam_min = int(os.environ["EXAM_MIN"])
        timedelta = int(os.environ["TIMEDELTA"])
    tzinfo = datetime.timezone(datetime.timedelta(hours=timedelta))
    curr_datetime = datetime.datetime.now(tz=tzinfo)
    curr_year = curr_datetime.year
    if curr_datetime > datetime.datetime(curr_year,
                                         exam_month,
                                         exam_day,
                                         exam_hour,
                                         exam_min,
                                         tzinfo=tzinfo):
        exam_datetime = datetime.datetime(curr_year + 1,
                                          exam_month,
                                          exam_day,
                                          exam_hour,
                                          exam_min,
                                          tzinfo=tzinfo)
    else:
        exam_datetime = datetime.datetime(curr_year,
                                          exam_month,
                                          exam_day,
                                          exam_hour,
                                          exam_min,
                                          tzinfo=tzinfo)
    return exam_datetime.timestamp()


@blueprint.route("/api/timestamp")
async def get_time():
    timestamp = await calc_exam_timestamp()
    json = {"timestamp": timestamp}
    return quart.jsonify(json)
