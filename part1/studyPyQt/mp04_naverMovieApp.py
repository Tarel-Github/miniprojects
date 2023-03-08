import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverApi import *
from urllib.request import urlopen
import webbrowser # 웹브라우저 모듈

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverApiMovie.ui', self)
        self.setWindowIcon(QIcon('./studyPyQt/newspaper.png'))

        # 검색버튼 클릭시그널 / 슬롯함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)# btnSearch는 naverApiSearch.ui 파일 안에 있음
        # 검색어 입력후 엔터를 치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)
    
    def tblResultDoubleClicked(self):
        # row = self.tblResult.currentIndex().row()
        # column = self.tblResult.currentIndex().column()
        # print(row, column)
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text()
        webbrowser.open(url) # 네이버 영화 웹사이트
            
    def txtSearchReturned(self):
        self.btnSearchClicked()


    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '영화명을 입력하세요!')
            return
        else:
            api = NaverApi() # NaverApi 클래스 객체 생성
            node = 'movie' # movie로 변경하면 영화를 검색할 수 있음
            display = 100

            result = api.get_naver_search(node, search, 1, display)
            print(result)
            # 테이블위젯에 출력 기능
            items = result['items'] # json결과 중 items 아래 배열만 추출
            self.makeTable(items) # 테이블위젯에 데이터들을 할당함수

    # 검색 버튼을 누르면테이블 위젯에 데이터 표시
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection) # 검색결과 테이블을 하나만 선택되도록 설정
        self.tblResult.setColumnCount(7) # 컬럼갯수 변경
        self.tblResult.setRowCount(len(items)) # 현재 100개 행을 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '개봉년도', '감독', '배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 60)
        self.tblResult.setColumnWidth(4, 50)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼데이터 수정 금지

        for i, post in enumerate(items): # 0, 뉴스
            title = self.replaceHtmlTag(post['title']) # HTML 특수문자 변환
            pubDate = post['pubDate']
            director = post['director']
            actor = post['actor']
            userRating = post['userRating']
            link = post['link']
            #image = QImage(requests.get(post['image'], stream = True))
            # imageUrl = urlopen(post['image']).read()            
            # image = QPixmap()
            # image.loadFromData(imageUrl)
            # imgLabel = QLabel()
            # imgLabel.setPixmap(QPixmap.fromImage(image))
            # imgLabel.setGeometry(0, 0, 60, 100)
            # imgLabel.resize(60, 100)
            # setItem(행, 열, 넣을 데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))
            #self.tblResult.setCellWidget(i, 6, imgLabel)
            #self.tblResult.setItem(i, 1, QTableWidgetItem(link))

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<').replace('&gt;', '>').replace('<b>', '').replace('</b>',
        '').replace('&apos;', "'").replace('&quot;', '"') #quotation mark 쌍따옴표
        # 변환 안된 특수문자가 나타나면 여기 추가

        return result

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())