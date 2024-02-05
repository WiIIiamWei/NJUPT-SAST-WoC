import requests
import pandas as pd

browse_header = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Host": "www.douyin.com",
    "Referer": "https://www.douyin.com/discover",
    "Cookie": "_xsrf=Pd0NpG6J8kZdHtzBVnNyQP1g0rO7NKeg; _zap=d7f27b9f-4fe3-4ef4-9376-df278af16940;"
}

url = "https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web"

res = requests.get(url, headers=browse_header).json()
# 实时上升热点
content_list = res['data']['word_list']
title_list = []
order_list = []
score_list = []
time_list = []
desc_list = []
url_list = []
index = 0
for content in content_list:
    index += 1
    order_list.append(content['position'])
    title_list.append(content['word'])
    score_list.append(content['hot_value'])
    time_list.append(content['event_time'])
    desc_list.append(content['word'])
    url_list.append(f"https://www.douyin.com/hot/{content['sentence_id']}")

df = pd.DataFrame({
    '热搜标题': title_list,
    '热搜排名': order_list,
    '热搜热度': score_list,
    '热榜时间': time_list,
    '链接地址': url_list
})
df.to_excel('../data/抖音热搜榜.xlsx', index=False)  # 保存结果数据