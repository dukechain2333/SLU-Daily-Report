from datetime import time, datetime
from time import sleep

from lixin1 import DailyReport

while 1:
    my_report = DailyReport(
        username="000000000", at_school=False, at_shanghai="在沪", ad_code="3101",
        covid_patient=0, teacher_id="00000000", school_name="未命名学院",
        class_name="未知班级", name="张三丰"
    )
    # :param username: [string] student ID
    # :param at_school: [true/false] if you're at school
    # :param at_shanghai: [string] options, "在沪"(in Shanghai), "在湖北"(in Hubei province),
    #     "在其它地区"(in other locations)
    # :param ad_code: [string] the first 4 digits of China administrative division code (different from postal code).
    #     Quick check: Shanghai "3101", your hometown as the first 4 digits of citizenship ID.
    #     For more details: http://preview.www.mca.gov.cn/article/sj/xzqh/2020/2020/202101041104.html
    # :param covid_patient: [int] options, 0 (health), 1 (suspected covid patient), 2 (covid patient).
    # :param teacher_id: [str] ID of your instructor in SLU
    #     Notes: You can check it in WeCom contact.
    # :param school_name: [str] name of your school
    #     Supported: 统计与数学学院, 信息管理学院, 财税与公共管理学院
    # :param class_name: [str] name of your class
    # :param name: [str] your name

    if time(hour=12, minute=0) <= datetime.now().time() <= time(hour=13, minute=0):
        result = my_report.run()
        print(result)
    else:
        print("Not in the reporting time period: ", datetime.now())
    sleep(3600)  # 1 hours (unit: seconds)
