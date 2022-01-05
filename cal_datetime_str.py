from datetime import datetime, timedelta
import re

def cal_date(target_str_dt:str, input_data: str) -> str:
    bad_input = _input_check(input_data)
    if bad_input:
        Exception
    format = _get_str_date_format(target_str_dt)
    target_dt = _str_convert_datetime(target_str_dt, format)
    ymd_list = _get_ymd_list(input_data)
    result_date = _calculate(target_dt, ymd_list)

def _calculate(date: datetime, ymd_list):
    for something in ymd_list:
        num = int(something[1:-1])
        if something[-1] == 'y':
            if something[:1] == '-':
                 date = date - timedelta(years=num)
            else:
                 date = date + timedelta(years=num)
        elif something[-1] == 'm':
            if something[:1] == '-':
                 date = date - timedelta(months=num)
            else:
                 date = date + timedelta(months=num)
        elif something[-1] == 'd':
            if something[:1] == '-':
                 date = date - timedelta(days=num)
            else:
                 date = date + timedelta(days=num)
        else:
            Exception

def _get_ymd_list(input_data: str) -> list: 
    ymd_list = re.findall('([+,-].+?[a-z])',input_data)
    return ymd_list

def _str_convert_datetime(target_dt, format) -> datetime:
    convert_date = datetime.strptime(target_dt, format)
    return convert_date

def _get_str_date_format(target_dt: str) -> str:
    format = '%Y-%m-%d'
    return format

def _input_check(input_data: str) -> bool:
    result = True
    ymd_list = re.findall('([+,-].+?[a-z])',input_data)
    if len(ymd_list) > 0:
        result = False
    return result