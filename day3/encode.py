
import sys
print(sys.getdefaultencoding())

s = "你哈"
print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))


s = "你哈"
s_gbk = s.encode("gbk")

print(s_gbk)
print(s.encode())

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print("utf8",gbk_to_utf8.decode("utf-8"))


