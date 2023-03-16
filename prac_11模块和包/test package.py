
# 包的导入:
# 1 :import 包名:

import message

# 2 : from 包名 import 模块名

from message import send_message
from message import receive_message

# 包的使用
# 1对应import:包名.模块名.函数名()

message.send_message.send()
message.receive_message.receive()

# 2对应from import:模块名.函数名()
send_message.send()
receive_message.receive()

# 要是在外界使用包中的模块,需要在__init__.py文件中指定对外界提供的模块列表
# 具体看那个文件  from.import 模块名
