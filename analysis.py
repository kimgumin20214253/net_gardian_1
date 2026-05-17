import pandas as pd
import numpy as np

def analyze_network_data():
    try:
        # 1. CSV 파일 읽기
        df = pd.read_csv('data.csv')
        
        if df.empty:
            print("데이터가 없습니다.")
            return None

        # 2. 통계 값 계산 (RTT 기준)
        avg_rtt = df['rtt'].mean()          # 평균 RTT
        max_rtt = df['rtt'].max()          # 최대 RTT
        p95_rtt = df['rtt'].quantile(0.95) # 상위 5% 지점 (95% Percentile)

        # 3. Threshold(임계치) 생성 
        # 보통 상위 5% 지점보다 조금 더 여유를 두어 기준을 잡습니다.
        threshold = p95_rtt * 1.2 

        print("--- 네트워크 분석 결과 ---")
        print(f"평균 RTT: {avg_rtt:.2f} ms")
        print(f"최대 RTT: {max_rtt:.2f} ms")
        print(f"95% Percentile RTT: {p95_rtt:.2f} ms")
        print(f"설정된 임계치(Threshold): {threshold:.2f} ms")
        print("--------------------------")

        return threshold

    except FileNotFoundError:
        print("data.csv 파일을 찾을 수 없습니다. 먼저 client.py를 실행해 주세요.")
        return None

if __name__ == "__main__":
    analyze_network_data()