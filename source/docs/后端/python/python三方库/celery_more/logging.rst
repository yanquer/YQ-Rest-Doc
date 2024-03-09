====================
日志
====================

celery 提供了自带的日志机制 get_task_logger::

  from celery.utils.log import get_task_logger

  logger = get_task_logger(__name__)

  @app.task
  def add(x, y):
      logger.info('Adding {0} + {1}'.format(x, y))
      return x + y


