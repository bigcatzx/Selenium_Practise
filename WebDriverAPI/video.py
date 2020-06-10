from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://videojs.com/")

video = driver.find_element_by_id("vjs_video_3_html5_api")

# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

sleep(10)

# 播放视频
print("start")
driver.execute_script("arguments[0].play()",video)

# 播放15s
print("Start Play for 15s")
sleep(15)

# 暂停视频
print("Pause")
driver.execute_script("arguments[0].pause()",video)

print("Quit Video")
driver.quit()