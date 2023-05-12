# 미니프로젝트 Part2
기간 - 2023.05.02 ~ 2023.05.16

## WPF 학습
- SCADA 시뮬레이션
    - C# WPF
    - MahApps.Metro(MetroUI 디자인 라이브러리)
    - Bogus(더미데이터 생성 라이브러리)
    - Newtonsoft.json
    - M2 Mqtt (통신 라이브러리)
    - DB 데이터바인딩
    - LiveCharts
    - OxyChart

- SmartHome 시스템 문제점
	- 실행 후 시간이 소요되면 UI제어가 느려짐 - TextBox에 텍스트가 과도
	- LiveCharts는 실시간 게이지외 대용량 데이터 차트는 무리(LiveCharts v.2 동일)
	- 대용량 데이터 차트는 OxyPlot를 사용

온습도 더미데이터 시뮬레이터
<img src="https://raw.githubusercontent.com/hugoMGSung/miniprojects/main/images/smarthome_publisher.gif" width="780" />

스마트홈 모니터링 앱
<img src="https://raw.githubusercontent.com/hugoMGSung/miniprojects/main/images/smarthome_monitor1.gif" width="780" />

스마트홈 모니터링 시각화
<img src="https://raw.githubusercontent.com/hugoMGSung/miniprojects/main/images/smarthome_monitor2.gif" width="780" />