from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
import sys

def create_screenshot_taker():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.set_window_size(1920, 1080*2)

    def take_screenshot(url, output_path, wait_time=3):
        try:
            os.makedirs(output_path, exist_ok=True)
            driver.get(url)
            time.sleep(wait_time)
            # 滚动一次滚轮, 去掉挡在上面的登录框
            driver.execute_script(f"window.scrollBy(0, 120);")  # 向下滚动
            time.sleep(0.5)  
            driver.execute_script(f"window.scrollBy(0, -120);") # 向上滚动
            time.sleep(0.5)  

            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.basename(output_path)
            screenshot_path = os.path.join(output_path, f"{filename}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)

        except Exception as e:
            print(f"Error taking screenshot: {e}")

    def close_driver():
        driver.quit()

    return take_screenshot, close_driver

if __name__ == "__main__":
    take_screenshot, close_driver = create_screenshot_taker()
    take_screenshot("https://www.bilibili.com", "bilibili")
    close_driver()

    