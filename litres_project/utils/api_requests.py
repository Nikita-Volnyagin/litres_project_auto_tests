import requests
import allure
from tests.api.conftest import base_url
from litres_project.utils.logging_helper import logging_helper


def api_get(url, **kwargs):
    with allure.step("API Request"):
        result = requests.get(base_url + url, **kwargs)
        logging_helper(result)
        return result


def api_post(url, **kwargs):
    with allure.step("API Request"):
        result = requests.post(base_url + url, **kwargs)
        logging_helper(result)
        return result


def api_put(url, **kwargs):
    with allure.step("API Request"):
        result = requests.put(base_url + url, **kwargs)
        logging_helper(result)
        return result
