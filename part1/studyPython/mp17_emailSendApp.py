# 이메일 보내기 앱
# 네이버 기준 2단계 인증을 해지해야 사용 가능
# send_pass에 올바른 비밀번호 입력
import smtplib # 메일전송프로토콜
from email.mime.text import MIMEText

send_email = 'sms_stmax@naver.com'
send_pass = '1234'# 임시 비밀번호
recv_email = 'nuntyem45@gmail.com'
smtp_name = 'smtp.naver.com'
smtp_port = 587 # 포트번호

text = '''어플을 통한 메일 보내기 태스트
빨리 작업 착수하자
'''
msg = MIMEText(text)
msg['Subject'] = '메일 제목입니다.'
msg['From'] = send_email # 보내는 메일
msg['To'] = recv_email # 받는 메일
print(msg.as_string())

mail = smtplib.SMTP(smtp_name, smtp_port) #SMTP 객체생성
mail.starttls() # 전송계층보안 시작
mail.login(send_email, send_pass)
mail.sendmail(send_email, recv_email, msg=msg.as_string())
mail.quit()
print('전송완료!')



