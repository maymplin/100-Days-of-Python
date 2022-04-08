import os
import requests
import datetime as dt
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
from_number = os.environ.get("TWILIO_PHONE_NUMBER")
to_number = os.environ.get("MOBILE_NUMBER")

today = dt.datetime.today()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_stock_price_difference():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }

    with requests.get(STOCK_API_ENDPOINT, params=stock_params) as response:
        response.raise_for_status()
        stock_data = response.json()["Time Series (Daily)"]

    yesterday_dt = today - dt.timedelta(1)
    day_before_dt = today - dt.timedelta(2)
    yesterday_str = yesterday_dt.strftime("%Y-%m-%d")
    day_before_str = day_before_dt.strftime("%Y-%m-%d")
    # yesterday_str = str(yesterday_dt).split(" ")[0]
    # day_before_str = str(day_before_dt).split(" ")[0]

    yesterday_close = float(stock_data[yesterday_str]["4. close"])
    day_before_close = float(stock_data[day_before_str]["4. close"])

    close_percentage_diff = (yesterday_close - day_before_close)/yesterday_close

    return close_percentage_diff*100


def trigger_alert(stock_close_difference):
    return stock_close_difference <= -5 or stock_close_difference >= 5


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_top_3_news():
    news_params = {
        "q": COMPANY_NAME,
        "from": str(today).split(" ")[0],
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }

    with requests.get(NEWS_API_ENDPOINT, params=news_params) as response:
        response.raise_for_status()
        news_data = response.json()

    top_3_news = news_data["articles"][:3]
    return top_3_news


def format_news_sms(news, stock_change):
    subject = f"{STOCK}: {'🔺' if stock_change > 0 else '🔻'}{abs(int(stock_change))}%"
    headline = f"Headline: {news['title']}"
    brief = f"Brief: {news['description']}"

    sms = f"{subject}\n{headline}\n{brief}"

    return sms


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

def send_sms(message):
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    sms = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    print(sms.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def stock_news_alert_app():
    price_diff = get_stock_price_difference()

    if trigger_alert(price_diff):
        top_3_news = get_top_3_news()

        for news in top_3_news:
            send_sms(format_news_sms(news, price_diff))


stock_news_alert_app()

print(get_top_3_news())
