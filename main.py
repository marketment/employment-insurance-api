from fastapi import FastAPI, Query
import requests
import xmltodict

app = FastAPI()

SERVICE_KEY = "iKOpfM3zIpKL5tQ/SHLRwuSj4Odbz2JaoWdkLiNdNSKr6jD3wo/sUJ/3+jdWEmvDLbNUZs8kY6QNzdhZs+eE/w=="

@app.get("/employment-insurance")
def get_insurance_info(
    bizCd: str = Query(..., description="보험 구분코드 (01: 고용, 02: 산재)"),
    pageNo: int = 1,
    numOfRows: int = 10
):
    url = "http://apis.data.go.kr/B490001/gySjbPstateInfoService/getEmpItm"
    params = {
        "serviceKey": SERVICE_KEY,
        "bizCd": bizCd,
        "pageNo": pageNo,
        "numOfRows": numOfRows
    }

    response = requests.get(url, params=params)
    xml_data = response.content
    dict_data = xmltodict.parse(xml_data)

    return dict_data