from background_task import background
from background_task.models import Task

from hallOfFameClient.stats.utility import calc_all_stats


@background(schedule=60)
def daily_task():
    calc_all_stats(True, False)


daily_task(repeat=Task.DAILY)