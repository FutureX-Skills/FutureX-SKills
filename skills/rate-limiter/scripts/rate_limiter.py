import time
import threading

class RateLimiter:
    """滑动窗口频率限制，线程安全"""
    def __init__(self, max_calls, period):
        self.max_calls = max_calls  # 窗口内最大调用次数
        self.period = period        # 时间窗口（秒）
        self.calls = []
        self.lock = threading.Lock()

    def acquire(self, block=True, timeout=30):
        """获取调用许可，block=True 时等待，False 时返回是否成功"""
        deadline = time.time() + timeout
        while True:
            now = time.time()
            with self.lock:
                self.calls = [t for t in self.calls if now - t < self.period]
                if len(self.calls) < self.max_calls:
                    self.calls.append(now)
                    return True
            if not block or time.time() > deadline:
                return False
            time.sleep(0.05)

    def __enter__(self):
        self.acquire(block=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# 预配置的常用限制器
class FeishuLimits:
    """飞书API频率限制配置"""
    CHAT_MESSAGE = (50, 1)      # 发送消息: 50次/秒
    FILE_UPLOAD = (5, 1)        # 文件上传: 5次/秒
    CONTACT = (20, 1)           # 通讯录: 20次/秒
    APP_TOKEN = (10, 1)         # 获取app_token: 10次/秒


class OpenAILimits:
    """OpenAI API频率限制配置"""
    GPT4_PER_MINUTE = (60, 60)  # GPT-4: 60次/分钟
    GPT35_PER_MINUTE = (200, 60)  # GPT-3.5: 200次/分钟


if __name__ == "__main__":
    # 示例用法
    rl = RateLimiter(max_calls=5, period=1.0)
    
    # 阻塞等待
    for i in range(10):
        rl.acquire(block=True)
        print(f"Call {i+1} at {time.time():.2f}")
    
    print("Done!")
