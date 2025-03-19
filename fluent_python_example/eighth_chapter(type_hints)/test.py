import pyautogui
personal_infomation_pos = (3140,206)
change_password_pos = (2960,515)
new_rock_info_pos = (2680,424)
new_project_info_pos = (2975,524)

aim_pos = new_rock_info_pos
pyautogui.moveTo(*aim_pos)
pyautogui.doubleClick(*aim_pos, duration=0.5)