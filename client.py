import time
from pymodbus.client import ModbusTcpClient
from save_data import save_network_data  # 1. 저장 함수 불러오기

def run_client():
    # 서버 접속 설정
    client = ModbusTcpClient('127.0.0.1', port=5020)
    
    if not client.connect():
        print("서버에 접속할 수 없습니다.")
        return

    try:
        while True:  # 연속적인 데이터 수집을 위해 반복문 추가
            # --- RTT 측정 시작 ---
            start_time = time.time()
            
            # 데이터 쓰기 및 읽기 작업 실행
            print("\n서버의 0번 서랍에 77을 입력 중...")
            write_result = client.write_register(0, 77)
            read_result = client.read_holding_registers(0, 1)
            
            # --- RTT 측정 종료 ---
            end_time = time.time()
            
            # 초 단위를 밀리초(ms)로 변환
            rtt = (end_time - start_time) * 1000
            
            # 통신 결과 확인 및 데이터 저장
            if not read_result.isError():
                val = read_result.registers[0]
                print(f"성공: 읽어온 값 {val} | RTT: {rtt:.2f}ms")
                # 정상 데이터 저장 (loss=0)
                save_network_data(rtt, 0, "normal")
            else:
                print(f"실패: 데이터를 읽지 못함 | RTT: {rtt:.2f}ms")
                # 손실 데이터 저장 (loss=1, status=abnormal)
                save_network_data(rtt, 1, "abnormal")

            # 1초 대기 후 다음 측정 (조절 가능)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n사용자에 의해 프로그램이 종료되었습니다.")
    finally:
        # 접속 종료
        client.close()
        print("서버 연결이 종료되었습니다.")

if __name__ == "__main__":
    run_client()