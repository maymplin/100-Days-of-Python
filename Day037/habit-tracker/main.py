# https://pixe.la/
# pytz time zones: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
# datetime strftime() method: https://www.w3schools.com/python/python_datetime.asp
# https://pypi.org/project/auto-py-to-exe/
# https://docs.python-requests.org/en/master/user/quickstart/

import requests
import os
import datetime as dt

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}

# graph_params = {
#     "id": "graph001",
#     "name": "Circadian - Morning Sun",
#     "unit": "minute",
#     "type": "int",
#     "color": "momiji",
#     "timezone": "America/Chicago",
# }


# create a pixela graph
# def create_graph(user_token, params):
#     with requests.post(url=graph_endpoint, json=params, headers=user_token) as response:
#         response.raise_for_status()
#         print(response.text)

# create_graph(headers, graph_params)

def create_graph(user_token, graph_id: str, graph_name: str, unit: str, unit_type: str, color: str, timezone="America/Chicago"):
    graph_params = {
        "id": graph_id,
        "name": graph_name,
        "unit": unit,
        "type": unit_type,
        "color": color,
        "timezone": timezone,
    }
    with requests.post(url=graph_endpoint, json=graph_params, headers=user_token) as response:
        response.raise_for_status()
        print(response.text)


# create_graph(headers, "graph002", "Circadian - Afternoon Sun", "minute", "int", "ichou")

# to view a created graph go to f"graph_endpoint/{graph_id}.html"
# e.g. https://pixe.la/v1/users/mlin/graphs/graph001.html


# add data a pixela graph
def post_pixel(user_token: str, graph_id: str, date: str, quantity: str):
    pixel_body = {
        "date": date,
        "quantity": quantity,
    }

    formatted_url = f"{graph_endpoint}/{graph_id}"

    with requests.post(url=formatted_url, json=pixel_body, headers=user_token) as response:
        response.raise_for_status()
        print(response.text)


# post_pixel(headers, "graph001", "20220407", "22")
# post_pixel(headers, "graph001", "20220408", "51")
# post_pixel(headers, "graph001", dt.datetime.today().strftime("%Y%m%d"), "64")
# post_pixel(headers, "graph002", dt.datetime.today().strftime("%Y%m%d"), "25")
# post_pixel(headers, "graph002", (dt.datetime.today() - dt.timedelta(1)).strftime("%Y%m%d"), "35")

# print(dt.datetime.today().strftime("%Y%m%d"))   #yyyymmdd


# update data on a pixela graph
def update_pixel(user_token, graph_id, date, quantity):
    updated_body = {
        "quantity": quantity,
    }

    update_pixel_url = f"{graph_endpoint}/{graph_id}/{date}"

    with requests.put(url=update_pixel_url, json=updated_body, headers=user_token) as response:
        response.raise_for_status()
        print(response.text)


# update_pixel(headers, "graph001", dt.datetime.today().strftime("%Y%m%d"), "52")

# delete data on a pixela graph
def delete_pixel(user_token: str, graph_id: str, date: str):
    delete_pixel_url = f"{graph_endpoint}/{graph_id}/{date}"

    with requests.delete(url=delete_pixel_url, headers=user_token) as response:
        response.raise_for_status()
        print(response.text)


# post_pixel(headers, "graph001", dt.datetime.today().strftime("%Y%m%d"), "51")
# post_pixel(headers, "graph002", dt.datetime.today().strftime("%Y%m%d"), "25")
# https://pixe.la/v1/users/mlin/graphs/graph001.html
