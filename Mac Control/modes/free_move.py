import pygame
import pyautogui

SMOOTHING_FACTOR = 3

DEAD_ZONE_THRESHOLD = 0.2

def free_move():
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    cursor_x, cursor_y = pyautogui.position()

    if joystick.get_numaxes() >= 2 and joystick.get_numbuttons() >= 1:
            BUTTON_A = 0
            BUTTON_B = 1
            BUTTON_X = 2
            BUTTON_Y = 3

            JOYSTICK_X = 0
            JOYSTICK_Y = 1

            TRIGGER_L = 4
            TRIGGER_R = 5

            if joystick.get_button(BUTTON_A):
                pyautogui.click()

            if joystick.get_button(BUTTON_B):
                pyautogui.rightClick()

            joystick_x_value = joystick.get_axis(JOYSTICK_X)
            joystick_y_value = joystick.get_axis(JOYSTICK_Y)

            if abs(joystick_x_value) > DEAD_ZONE_THRESHOLD or abs(joystick_y_value) > DEAD_ZONE_THRESHOLD:
                target_x = cursor_x + joystick_x_value * 25
                target_y = cursor_y + joystick_y_value * 25
                cursor_x += (target_x - cursor_x) * SMOOTHING_FACTOR
                cursor_y += (target_y - cursor_y) * SMOOTHING_FACTOR

                cursor_x = max(0, min(cursor_x, pyautogui.size()[0]))
                cursor_y = max(0, min(cursor_y, pyautogui.size()[1]))

                pyautogui.moveTo(cursor_x, cursor_y, duration=0)