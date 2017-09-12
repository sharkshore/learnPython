#!/usr/bin/python3
import socket
import sys
import time

serversocket=socket.socket( socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port=9999

serversocket.bind((host,port))
serversocket.listen(5)
while True:
	client,add=serversocket.accept()
	print("连接地址: %s" % str(add))
	msg="欢迎访问菜鸟教程！"+ "\r\n" + "当前时间为:"+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	client.send(msg.encode('utf-8'))
	client.close()
