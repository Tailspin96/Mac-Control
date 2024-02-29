import pygame

from updater.app_updater import check_for_update
from messages import notifications
from modes import modes_list
from modes import free_move

CURRENT_MODE = None

update_check_triggered = False
update_check_completed = False

mode_changed_free_move_triggered = False

joystick_not_connected_message_triggered = False
joystick_connected_message_triggered = False

pygame.init()
pygame.joystick.init()
pygame.event.get()
pygame.event.set_blocked(pygame.ACTIVEEVENT)

while True:
    pygame.event.get()

    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        if not joystick_connected_message_triggered:
            notifications.notificationBalloon("Mac Control", joystick.get_name() + " has connected")
            joystick_connected_message_triggered = True
            joystick_not_connected_message_triggered = False

        if joystick.get_numaxes() >= 2 and joystick.get_numbuttons() >= 1:
            TRIGGER_L = 4
            TRIGGER_R = 5

            BUTTON_MINUS = 4
            BUTTON_PLUS = 6

            if joystick.get_button(BUTTON_PLUS):
                if not mode_changed_free_move_triggered:
                    CURRENT_MODE = modes_list.Move_Mode.FREE_MOVE
                    notifications.notificationBalloon("Mac Control", "Mode changed to Free Move")
                    mode_changed_free_move_triggered = True

            if CURRENT_MODE == modes_list.Move_Mode.FREE_MOVE:
                free_move.free_move()
            elif CURRENT_MODE == modes_list.Move_Mode.SNAP_MOVE:
                notifications.notificationBalloon("Mac Control", "This feature is not implemented yet")

            if joystick.get_axis(TRIGGER_L) >= 0.5 and joystick.get_axis(TRIGGER_R) >= 0.5:
                if not update_check_triggered:
                    check_for_update()
                    update_check_triggered = True
            else:
                update_check_triggered = False

        else:
            print("Joystick does not have the required number of axes or buttons.")
    else:
        if not joystick_not_connected_message_triggered:
            print("No joysticks detected.")
            notifications.notificationBalloon("Mac Control", "No controller detected")
            joystick_not_connected_message_triggered = True
            joystick_connected_message_triggered = False


