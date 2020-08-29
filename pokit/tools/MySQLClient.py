"""
Created by hu-jinwen on 2020/8/29

python访问mysql
"""
import MySQLdb


class MySQLClient(object):
    """mysql客户端"""

    def __init__(self, host, db, user, passwd, port=3306):
        """
        初始化
        :param host:
        :param db:
        :param user:
        :param passwd:
        :param port:
        """
        self.__host = host
        self.__port = port
        self.__db = db
        self.__user = user
        self.__passwd = passwd

        self.__connection = MySQLdb.connect(
            host=host,
            port=port,
            db=db,
            user=user,
            passwd=passwd
        )

    def select(self, sql):
        """"""
        cursor = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        finally:
            if cursor:
                cursor.close()

    def close(self):
        """"""
        self.__connection.close()
