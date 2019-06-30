import json
import os

def print_exception(function_name, error, response):
    print("request: " + function_name + " - status_code: " + str(response.status_code) + " - message: " + response.text)
    print("\n\n")
    print(">>>>>" + function_name + str(error))


def generate_data_file(**data):
    return data


def generate_header(**header):
    if header != {}:
        header['content-type'] = header.pop('content_type')
    else:
        header = generate_header(content_type='application/json')
    return header


def generate_url_with_param(url, param):
    if param is not None:	
        for index, key in enumerate(param):
            if index == 0:
                url = url + '?' + str(key) + '=' + str(param[key])
            else:
                url = url + '&' + str(key) + '=' + str(param[key])
    return url


def generate_report(system):
    if system.lower() == 'win':
        os.system("powershell.exe -Command '& allure generate allure-results --clean -o allure-html'")
        os.system("ren allure-html' allure-html")

    elif system.lower() == 'mac':
        os.system("allure generate allure-results --clean -o allure-html")