# 12
import time

def focus_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds

    print(f"Focus timer set for {minutes} minutes.")

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end="\r", flush=True)
        time.sleep(1)

    print("Focus timer completed.")

# 在这里设置你想要的专注时间（单位：分钟）
focus_time = 25

# 启动专注时钟
focus_timer(focus_time)
