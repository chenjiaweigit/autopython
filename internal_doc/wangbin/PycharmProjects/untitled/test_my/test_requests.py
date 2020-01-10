# coding: utf-8
import requests
import json

# r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
# print(r.status_code)  # 获取返回状态
# r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
# print(r.url)
# # print(r.text)  # 打印解码后的返回数据
# r = requests.get('https://github.com/timeline.json')
# r.json()

if __name__ == '__main__':

    json_301 = {"did": "ffffffff-f4i$'x9f700ii37=;9:52<{}ja",
     "emulatordid": "",
     "grp": "winretailsaler",
     "imei": "862858039377872",
     "lang": "zh_CN",
     "platform": "crma_winretailsaler",
     "smDid": "Dutg4pd2EyPavpAn3trS2tS0eh92IW9bLLwi0jNjfkbE2a8jQkwYDPgo44vm4KR7FDu6eBsElprgBXZOqmu/sbHg",
     "src": "huawei",
     "token": "6708204011111111111111111369662821949379",
     "ver": "1.7.6",
     "wifi": "02:00:00:00:00:00"}
    str_content = json.dumps(json_301)

    url = "http://retail.wincrm.net:8202/plugin.servlet?type=301&info=VTJGc2RH" \
          "VmtYMTkyRmZwNlhwR3IyNjRVZTFBSHhPZGkvcFlxTmhtZlVqbWcxRXB6MnQ0SWgyNjZaWmp" \
          "2Ukp4NgpIMVBJQ0NtL1RWb1h1TGNGRUQ3S2JkekR3RkMvUmxFQnkwQ3l6TjBpWEtBMm9hbjlBMlJVaj" \
          "RRcjhRRzJHNU42CndlVjVRemxrcjJTUG9JY3FLWXZqaHJHUzY3SUJOWTZzM3l2Z3hrZ2FlREVNdXZaNjEyRF" \
          "craDE1ZUdwclZKVlUKd1cvKzRLUTRyN1AvMDM5MGJ3TVlRdk84WWtWVG5NOG0yYXJVWW9mUGdJUkhPeGs0QzJLSD" \
          "luMVNBN3k2NUZuWApKcDNzbVlVa2hQR1htSkwwclRMRmlzTWQvWlhhZlhuTzB1Y1VPM0VQdjl2SFJzLzA1VHlFSVlhNE" \
          "NNSHVOZis2CjMvaVVpd0tJQ2UxaFcybEpzbE9hZmZyVTcwSlprWGtLaUloLzRFMTJ1N3E1WGQ2ajBDc1pmYlEzOHhJQ1VJT" \
          "GUKMXhTU0EwK0hOWUZMUzZHT0hhUzFNNUJlWTAwckJnRTVLVEU2UDhYdGdxQkZXSVFaZVNxOHcwRXZhUVBSd2M0SQpCY0Ryamd" \
          "lc1h2ditYdTgxUHVzaXlQYjNaV0dnQXo0WmNQbU9mRjlEZWx6cTh1UnN6N0tRN2V3VHllQzJUSkxUClIydUpBVVBVRkJqVHZHU1E1W" \
          "URkM1VnYVdUd2luM0F0TEJyTGMxZ1htQVNIcGRrYXdXNWp3ODdidVNOTWt5L3cKKzErckMrY1oxVVdSR2l6ZkFFMzh6dHJ4OUFvTzdoaUd2" \
          "NTc2YXlaZURTWDV2SnFjMVQrUHhVMUVLamRKM1Y4WApVWENUaGRHN3FCMUUwK1pBd1dvdXZqeGdsNzRta0txTjZPN0JPcWQySnBkM0oyaVN1M" \
          "2ZBVE1DUGREYmdWYmdYCmV4L2xTQUthak85emNzZ094WktDeGpqeTliTG9JMnJ5MWFHQzRQWElreHRIM3VrOHhHY3pmN2JuaytlNnZRVVo="
    r = requests.get(url, json=str_content)
    # r.encoding='utf-8'
    print(r.text)
    print(r.encoding)
    print(r.content)



    # requests.get(json_301)