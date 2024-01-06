import requests

# 네이버 API 설정, # 네이버 애플리케이션의 Client ID, # 네이버 애플리케이션의 Client Secret 를 넣어야 함 
client_id = "NAVER API CLIENT ID"
client_secret = "NAVER API CLIENT KEY"


def search_news(keyword):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    params = {
        "query": keyword,
        "display": 50  # 검색 결과 출력 개수 설정
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()
    print(data)

    # 검색 결과 출력
    # for item in data['items']:
    #     title = item['title']
    #     link = item['link']
    #     print("제목:", title)
    #     print("링크:", link)
    #     print()

# 검색어를 입력하여 뉴스 검색 수행
search_news("SEARCH KEYWORD")


