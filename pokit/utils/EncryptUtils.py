"""
Created by joe on 2020/7/3
"""
import base64
import hashlib
import urllib

from pokit.tools import LoggerFactory

logger = LoggerFactory.get_logger("EncryptUtils")

# 缺少依赖 pycrypto。不影响使用，但是某些方法用不了。windows上安装 pycrypto 确实太麻烦了。
try:
    from Crypto.Cipher import PKCS1_v1_5
    from Crypto.PublicKey import RSA
except Exception:
    logger.warn("""
    You have no installed pycrypto dependency. It doesn't affect your use, but you can't use the rsa_encode method.
    """)


def url_encode(string):
    """
    url encode
    """
    return urllib.parse.quote(string, safe='/', encoding=None, errors=None)


def rsa_encode(pub_key, _str):
    """
    RSA 加密
    :param pub_key: 公钥
    :param _str: 待加密字符串
    :return:
    """
    rsa_key = RSA.importKey(pub_key)
    cipher = PKCS1_v1_5.new(rsa_key)
    result = base64.b64encode(cipher.encrypt(bytes(_str, encoding="utf-8")))
    return str(result, encoding="utf-8")


def md5(_str):
    """
    字符串做md5
    :param _str:
    :return:
    """
    return hashlib.md5(_str.encode('utf-8')).hexdigest()
