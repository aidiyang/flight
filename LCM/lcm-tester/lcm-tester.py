import lcm

lc = lcm.LCM()

from lcmt_tvlqr_controller_action import lcmt_tvlqr_controller_action

msg = lcmt_tvlqr_controller_action();

msg.timestamp = 0;

msg.trajectory_number = 1;

lc.publish("tvlqr-action", msg.encode())
