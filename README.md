# 문자 갯수 세기
이 프로그램은 국어수행의 문자가 200자가 넘어야하는데 ".",",",띄어쓰기 는 갯수에 포함하지 않아야 합니다.
그렇기때문에 몇자가 되는지 세기가 힘들어 만들게 되었습니다.
----사용법-------
200자를 쓸때는 한줄이 아니라 여러줄이기 때문에
여러줄을 계속 입력을 받다가
끝나면 다음줄에 *이 입력되면
------코드-------
![image](https://user-images.githubusercontent.com/88232976/164592899-f72ff901-8777-4f13-be8f-bf45288edab3.png)
----설명---------
while문으로 무한반복을 돌려서 입력을 받습니다.(여러줄을 입력받기 위함)<br>
그리고 마지막에 *이 입력되면 무한반복에서 나가게 조건문으로 설정해주고<br>
아니면 a에 그 리스트로 바꾼 문자열을 더합니다.<br>
그리고 무한반복에서 나가면 for문으로 조건으로 <strong>"."</strong>,<strong>","</strong>,<strong>띄어쓰기</strong> 는 세지 않게 조건을 만들었습니다.
