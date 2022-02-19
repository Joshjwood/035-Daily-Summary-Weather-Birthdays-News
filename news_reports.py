import requests
import datetime
from privates import *

YESTERDAY = datetime.timedelta(days=1)

NEWS_API = NEWS_API
NEWS_ENDPOINT = NEWS_ENDPOINT


def bbc_today():
    news_params = {
        "apiKey": NEWS_API,
        "sources": "bbc-news",
        "sortBy": "popularity",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    ###########################
    report = "BBC News: \n"
    for i in range(0, 3):
        report += news_data["articles"][i]["title"] + "\n"
        report += news_data["articles"][i]["description"] + "\n\n"
    return report

def reuters_today():
    news_params = {
        "apiKey": NEWS_API,
        "sources": "reuters",
        "sortBy": "popularity",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    ###########################
    report = "Reuters: \n"
    for i in range(0, 3):
        report += news_data["articles"][i]["title"] + "\n"
        report += news_data["articles"][i]["description"] + "\n\n"
    return report

def guardian_today():
    news_params = {
        "apiKey": NEWS_API,
        "sources": "the-verge",
        "sortBy": "popularity",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    ###########################
    report = "The Verge: \n"
    for i in range(0, 3):
        report += news_data["articles"][i]["title"] + "\n"
        report += news_data["articles"][i]["description"] + "\n\n"
    return report

def yesterday_top_3():
    news_params = {
        "apiKey": NEWS_API,
        "country": "gb",
        # "qInTitle": COMPANY_NAME,
        "from": YESTERDAY,
        "sortBy": "popularity",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    ###########################
    report = "Top 3 stories from Yesterday: \n"
    for i in range(0, 3):
        report += news_data["articles"][i]["title"] + "\n"
        report += news_data["articles"][i]["description"] + "\n\n"
    return report