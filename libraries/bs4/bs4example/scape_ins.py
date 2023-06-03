import requests
from bs4 import BeautifulSoup
from typing import List, Tuple
import pandas as pd


def get_clinic_name(clinic_id: int)-> str:
    url: str = f"https://{clinic_id}.portal.athenahealth.com"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    clinic_name = soup.find_all("h1")[-1].text.strip()
    return clinic_name


def get_all_clinics(start: int, end: int)-> None:
    master_list = []
    match (start, end):
        case (s, e) if s > e:
            return "start param greater than end"
        case _:
            for clinic_id in range(start, end+1):
                data_dict = {}
                data_dict["clinic_id"] = clinic_id
                data_dict["clinic_name"] = get_clinic_name(clinic_id)
                master_list.append(data_dict)
    return master_list


start = 12690
end = 12710

pd.DataFrame(get_all_clinics(start, end)).to_html("clinics.htm;", justify="center")





    
                

    