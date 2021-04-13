import asyncio
from education.interface.updatewg import UpdateWg
from education.common.wechat import *

# if __name__ == '__main__':
#     async def running(i):
#         print("-------------第{}个任务：任务开始启动---------------".format(i))
#         startWork = UpdateWg()
#         startWork.selectInstance()
#         startWork.updateDevices()
#         startWork.startDevices()
#         await asyncio.sleep(i)
#         print("------------第{}个任务完成-----------".format(i))
#
#
#     async def report():
#         print("------任务正在执行-------")
#
#     for i in range(50):
#         loop = asyncio.get_event_loop()
#         tasks = [
#             asyncio.ensure_future(running(1)),
#             asyncio.ensure_future(running(2)),
#             asyncio.ensure_future(running(3)),
#             asyncio.ensure_future(running(4)),
#             asyncio.ensure_future(running(5)),
#             asyncio.ensure_future(report())
#         ]
#         loop.run_until_complete(asyncio.wait(tasks))

if __name__ == '__main__':
    startWork = UpdateWg()
    startWork.selectInstance()
    startWork.updateDevices()
    startWork.startDevices()
    send_msg()