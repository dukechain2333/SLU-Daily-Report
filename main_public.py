from datetime import time, datetime
from time import sleep

from lixin1 import DailyReport

my_report = DailyReport(
        username="000000000", at_school=False, at_shanghai="在沪", ad_code="3101",
        covid_patient=0, teacher_id="00000000", school_name="未命名学院",
        class_name="未知班级", name="张三丰"
    )

while 1:
    if time(hour=12, minute=0) <= datetime.now().time() <= time(hour=13, minute=0):
        result = my_report.run()
        print(result)
    else:
        print("Not in the reporting time period: ", datetime.now())
    sleep(3599)  # 1 hours (unit: seconds)
