=================
click
=================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


``click`` 是对 ``Argparse`` 进行封装后的一个 python 命令行工具
(类似 ``request`` 对 ``urllib`` 的封装)

命令行工具, 使用装饰器配置选项参数.

- 普通形式_ , 一个函数上打上所有选项参数
- 组_ , 以组的形式使用


普通形式
=================

如::

  import sys

  import click

  @click.command()        # 表示包装为 click 指令
  @click.option('-u', '--user', type=str, help='username')         # 添加选项参数
  @click.option('-p', '--password', type=str, help='password')         # 添加选项参数
  @click.option('-a', '--about', type=str, help='about message', default=None, show_default=True)         # 添加选项参数
  @click.option('--admin', type=bool, default=False)         # 添加选项参数
  def run(user: str, password: str, about: str='about message', admin: bool = False):

      if user == 'xxx':
          click.echo('login failed', err=True)
          return
      elif user and password:
          click.echo('login success')
      if admin:
          click.echo('you are a admin')
      click.echo(f'{about = }')


  if __name__ == '__main__':
      run(sys.argv[1:])

效果::

  yanque@yanquedembp with_click % python click_one_f.py --help
  Usage: click_one_f.py [OPTIONS]

  Options:
    -u, --user TEXT      username
    -p, --password TEXT  password
    -a, --about TEXT     about message
    --admin BOOLEAN
    --help               Show this message and exit.
  yanque@yanquedembp with_click % python click_one_f.py
  about = None
  yanque@yanquedembp with_click % python click_one_f.py -u xxx -p xxx
  login failed
  yanque@yanquedembp with_click % python click_one_f.py -u xxxx -p xxx
  login success
  about = None



组
=================

创建组，就是通过一个主入口函数，去关联其他的函数，其他的函数名可以作为命令直接使用::

  import sys
  import click

  @click.group()
  def main():
      ...

  @main.command()        # 表示包装为 click 指令
  @click.option('-u', '--user', required=True, type=str, help='username')         # 添加选项参数
  def login_user(user: str):
      ...

  @main.command()
  @click.option('-p', '--password', required=True, type=str, help='password')         # 添加选项参数
  def login_password(password: str):
      ...

  if __name__ == '__main__':
      main(sys.argv[1:])

效果::

  yanque@yanquedembp with_click % python click_group_f.py --help
  Usage: click_group_f.py [OPTIONS] COMMAND [ARGS]...

  Options:
    --help  Show this message and exit.

  Commands:
    login-password
    login-user


使用
=============

支持单函数使用与group分组使用

- @click.group()	分组使用
- @click.command()	作为命令行选项使用
- @click.argument()	位置参数
- @click.option()	关键字参数
  - default
  - type
  - help
  - show_default

.. code-block:: python

  import click


  @click.command()
  @click.option('-m', '--msg', help='this is use to echo a msg')
  def show_msg(msg):
    click.echo('input ' + msg)


  @click.command()
  @click.option('-i',             # 短选项
        '--int_v',        # 长选项， 注意与函数的参数名一致
        # type=int,
        default=1,        # 用默认值就可以不用 type=int
        help='echo a int value',
        show_default=True)
  def show_int(int_v: int):
    click.echo('input ' + str(int_v))


  @click.command()
  @click.argument('name')         # 相当于 python 位置参数
  @click.option('-i',             # 短选项， 相当于 python 关键字参数
        '--int_v',        # 长选项， 注意与函数的参数名一致
        # type=int,
        default=1,        # 用默认值就可以不用 type=int
        help='echo a int value',
        show_default=True)
  def show_int2(name, int_v: int):
    click.echo('input ' + name + str(int_v))


  @click.group()
  def use_group():
    pass


  @use_group.command(help='show a msg')
  @click.option('-m', '--msg', help='this is use to echo a msg')
  def group_show_msg(msg):
    click.echo('input ' + msg)


  @use_group.command(help='show a integer msg')
  @click.option('-i',             # 短选项
        '--int_v',        # 长选项， 注意与函数的参数名一致
        # type=int,
        default=1,        # 用默认值就可以不用 type=int
        required=True,
        help='echo a int value',
        show_default=True)
  def group_show_int(int_v: int):
    click.echo('input ' + str(int_v))


  def main():
    # # 单个使用方式， 直接调用函数, 一次只能用一个
    # # 使用默认值的调用 python3 t_click.py， 输出 input 1
    # # 不使用默认值的调用 python3 t_click.py -i 10， 输出 input 10
    # show_int()
    # # show_msg()

    # group 组的形式， 组会自动关联所有可调用函数(即command)
    # 一次只能使用一个选项
    # python3 t_click.py group-show-msg -m tt
    #   输出 input tt
    # python3 t_click.py group-show-int
    #   输出 input 1
    use_group()


  if __name__ == '__main__':
    main()


非装饰器调用
=============

- click.echo(...)				类似于 print
- click.ClickException(...)		rasie使用
- click.get_current_context()	获取全局上下问, 单线程内有效

