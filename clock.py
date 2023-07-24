python
import time
import winsound

focus_minutes = 25 # 专注时长,单位分钟
rest_minutes = 5   # 休息时长,单位分钟 

while True:
  print("Focus time start!")
  start_time = time.time()
  while time.time() < start_time + focus_minutes*60:
    print("\rFocusing: %d seconds passed" % (time.time() - start_time), end='')
    time.sleep(1)
  
  print("\nRest time start!") 
  winsound.Beep(600, 500) 
  start_time = time.time()
  while time.time() < start_time + rest_minutes*60:
    print("\rResting: %d seconds passed" % (time.time() - start_time), end='') 
    time.sleep(1)

  winsound.Beep(600, 500)
