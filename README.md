# SLU Daily Report
 Auto daily COVID-19 epidemic prevention report in Shanghai Lixin University of Accounting and Finance 

![](https://img.shields.io/badge/tests-2021.1.18%20%E2%9C%94-green)

## Introduction

**Student 2021 Version**

**Shanghai Lixin University of Accounting and Finance**

The university requires students and teachers to report their health conditions, locations and other information daily. Since it is at low efficiency to report manually everyday, I develop a script to automatically complete the task.

## Usage

1. Develop the script in your desktop PC or cloud server.

2. Download this package and save.

3. Fill your personal information in `main.py`.

4. Windows: <br />
   Run `main.py` with python >= 3.7. <br />
   Linux: <br />
   (1) If you do not have `screen` package.

   ```bash
   # For CentOS
   yum -y install screen
   # For Debain/Ubuntu
   apt install screen
   ```

   (2) Run the following command. Tested pass for python >= 3.7.

   ```bash
   screen
   pip3 install -r requirements
   cd [INSTALLED FOLDER]
   python3 main.py
   ```

5. Keep this program running 24 hours a day & 7 days a week.

Guidance for filling personal information:

| Parameters Name | Data Type | Description                                                  |
| --------------- | --------- | ------------------------------------------------------------ |
| username        | string    | student ID                                                   |
| at_school       | bool      | if you're at school                                          |
| at_shanghai     | string    | options: "在沪"(in Shanghai), "在湖北"(in Hubei province), "在其它地区"(in other locations) |
| ad_code         | string    | the first 4 digits of China administrative division code (different from postal code).<br />Quick check: Shanghai "3101", your hometown as the first 4 digits of citizenship ID.<br />For more details: http://preview.www.mca.gov.cn/article/sj/xzqh/2020/2020/202101041104.html |
| covid_patient   | int       | options, 0 (health), 1 (suspected covid patient), 2 (covid patient). |
| teacher_id      | string    | ID of your instructor in SLU<br />Notes: You can check it in WeCom (Wechat Work / WXWork) contact. |
| school_name     | string    | name of your school<br />Supported: 统计与数学学院, 信息管理学院, 财税与公共管理学院 |
| class_name      | string    | name of your class                                           |
| name            | string    | your name                                                    |

## Attached Tools

`header_python_decorator.py` is a tool to convert Chrome formatted web request/response headers to Python formatted ones.

For example, it can convert this header,

```yaml
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
```

to the following header.

```python
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
```

To use this tool, put the original header into the text file `header_converter_space`, and run `header_python_decorator.py`.
