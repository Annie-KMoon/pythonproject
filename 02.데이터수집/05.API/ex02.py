#할리스 서울 매장정보
import requests
import json
import os

def getAddress():
    with open('data/hollys.json', 'r',encoding='utf-8')as file:
        address = json.load(file)
        # print(address) #파일 로드 확인

query='전북 삼성동 100'
url=f'https://dapi.kakao.com/v2/local/search/address.json?query={query}'
headers = {'Authorization': 'KakaoAK 3b1f91160f090c6816a03b93720659b4'}
res =requests.request(method='get', url=url, headers=headers)
print(res)