"""
Created by hu-jinwen on 2020/8/29
"""
from pokit.tools.MySQLClient import MySQLClient

mysql_client = MySQLClient("10.0.0.38", "fbi", "fbimysql", "Fbimysql@12426")

sql = """SELECT 1 AS `type`, url, url_md5, is_serial,is_original,protect_days,filter_start_time,filter_end_time,crawler_times FROM fbm_video_download_task
 WHERE is_serial = '1' AND STATUS = 1 AND (end_time IS NULL OR end_time > NOW()) AND works_id  IN (SELECT a.works_id FROM  fbo_receive_api a WHERE 
  a.`fbccKey` = 24939596 AND a.`status` = 1) AND url LIKE '%sec_uid%'  ORDER BY crawler_times"""

result = mysql_client.select(sql)

mysql_client.close()
