import socket
import sys


# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口好
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))


msg=s.recv(1024)
s.close()
print(msg.decode('utf-8'))



