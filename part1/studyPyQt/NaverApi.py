# NaverApi 클래스 - OpenAPI 인터넷을 통해서 데이터를 전달 받음
from urllib.request import Request, urlopen
from urllib.parse import quote
import datetime # 현재시간 사용
import json # 결과는 json으로

class NaverApi:
    # 생성자
    def __init__(self) -> None:
        print(f'[{datetime.datetime.now()}]Naver API 생성')

    # Naver API를 요청 함수
    def get_request_url(self, url):
        req = Request(url)
        # Naver API 개인별 인증
        req.add_header('X-Naver-Client-Id','J7uUVrLMveirFsTQByuz') # Naver 개발자에서 애플리케이션 정보 코드를 가져옴
        req.add_header('X-Naver-Client-Secret','ebONuWSQnu')  #Naver 개발자 애플리케이션 정보의 시크릿 정보 코드를 가져옴

        try:
            res = urlopen(req) # 요청 결과가 바로 돌아옴
            if res.getcode() == 200: # response OK
                print(f'[{datetime.datetime.now()}]NaverAPI 요청 성공 []')
                return res.read().decode('utf-8')
            else:
                print(f'!!! [{datetime.datetime.now()}]NaverAPI 요청 실패 !!!')
                return None
        except Exception as e:
            print(f'[{datetime.datetime.now()}] 예외발생 {e}')
            return None

    # 실제 호출함수
    def get_naver_search(self, node, search, start, display):
        base_url = 'https://openapi.naver.com/v1/search'#네이버 api를 가져올 때는 이런 형태로 작성
        node_url = f'/{node}.json'
        params = f'?query={quote(search)}&start={start}&display={display}'

        url = base_url + node_url + params
        retData = self.get_request_url(url)

        if retData == None:#에러 등으로 인해 리턴값이 없는 경우 
            return None
        else:
            return json.loads(retData) # json으로 return.



    # # json 데이터를 list로 변환, 필요없어져서 주석처리
    # def get_post_data(self, post, outputs) -> None:
    #     title = post['title']
    #     description = post['description']
    #     originallink = post['originallink']
    #     link = post['link']

    #     # 'Tue, 07 Mar 2023 17:04:00 +0900' 문자열로 들어온걸 날짜형으로 변경
    #     pDate = datetime.datetime.striptime(post['pubDate'], '%a, %d, %b, %Y, %H:%M:%S +0900')
    #     pubDate = pDate.strftime('%Y-%m-%d %H:%M:%S') # 2023-03-07 17:04:00 우리가 쓰는 형태로 변경

    #     # outputs에 옮기기 - TO BE CONTINUED...
    #     outputs.append({'title':title, 'description':description,
    #                     'originallink':originallink, 'link':link,
    #                     'pubDate':pubDate})
    