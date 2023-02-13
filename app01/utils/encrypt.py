import hashlib
from   django.conf import settings

def md5(data_string):
    # 创建一个 MD5 对象
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    # 更新 MD5 对象，输入要进行哈希的数据字符串
    obj.update(data_string.encode('utf-8'))
    # 返回数据字符串的十六进制形式的哈希值
    return obj.hexdigest()
