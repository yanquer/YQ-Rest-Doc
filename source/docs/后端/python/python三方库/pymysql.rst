================
pymysql
================

安装::

  pip install pymysql

提供数据库操作::

  import pymysql

  db = pymysql.connect(
      host='127.0.0.1',
      user='user',
      password='password',
      database='database'
  )

  cur = db.cursor()

  try:
      cur.execute('show tables;')
      result = cur.fetchone()
      print(result)

      cur.execute('select user();')
      result = cur.fetchone()
      print(result)
      db.commit()
  except Exception as e:
      db.rollback()
  finally:
      db.close()


