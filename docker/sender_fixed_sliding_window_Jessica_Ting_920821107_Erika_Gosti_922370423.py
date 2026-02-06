# measure and report the (a) throughput (size of transmitted data/time taken to
# send data) in the units of bytes per second , (b) the average per-packet delay in the units of seconds and at the
# end, (c) the performance of the UDP sender.
# (a) To measure throughput, start your timer as soon as you create your socket and stop your timer once
# you have received acknowledgments for all packets. You have to include sequence numbers in your
# packets to keep track of acknowledgments.
# (b) To measure the per-packet delay, you will start your timer when you send the packet and stop the
# timer when you receive an acknowledgment from the receiver for that packet. In case of
# retransmissions, you should consider the timer to start when you send the packet the first time and stop
# the timer when you finally receive the acknowledgement.
# (c) To evaluate the performance of your UDP sender, you are required to compute the following metric:
# 𝑀𝑒𝑡𝑟𝑖𝑐 = 0. 3 𝑇ℎ𝑟𝑜𝑢𝑔ℎ𝑝𝑢𝑡/1000 + 0. 7/𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝐷𝑒𝑙𝑎𝑦 𝑝𝑒𝑟 𝑃𝑎𝑐𝑘𝑒𝑡