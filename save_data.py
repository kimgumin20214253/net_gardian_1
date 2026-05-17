import csv
import os
from datetime import datetime

# 데이터가 저장될 파일명
FILE_NAME = "data.csv"

def save_network_data(rtt, loss, status="normal"):
    """
    네트워크 통신 데이터를 CSV 파일에 저장하는 함수
    :param rtt: 응답 시간 (ms)
    :param loss: 패킷 손실 여부 (0 또는 1)
    :param status: 정상/이상 판단 결과 (기본값: normal)
    """
    
    # 현재 시간 가져오기
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 파일이 존재하는지 확인 (헤더 추가 여부 결정)
    file_exists = os.path.isfile(FILE_NAME)
    
    # 데이터 한 줄 작성
    with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # 파일이 처음 생성되는 경우에만 헤더(열 이름)를 추가
        if not file_exists:
            writer.writerow(["time", "rtt", "loss", "status"])
        
        # 데이터 입력
        writer.writerow([now, rtt, loss, status])

if __name__ == "__main__":
    # 테스트용 데이터 (직접 실행했을 때 작동 확인)
    print("데이터 저장 테스트 중...")
    save_network_data(10.5, 0, "normal")
    save_network_data(500.2, 1, "abnormal")
    print(f"'{FILE_NAME}' 파일에 데이터가 저장되었습니다.")