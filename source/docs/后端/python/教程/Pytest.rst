=====================
Pytest使用
=====================

搜索范围
=====================

先找到当前目录下以test_为前缀和以_test为后缀的文件,

然后在其中搜索:

- 以test为前缀的函数
- 以Test为前缀的类(注意一般测试类不应包含__init__()函数)中以test为前缀的函数
- 继承unittest.TestCase单元测试类中, 以test为前缀的函数


选项参数
=====================

-v, -q 	打印用例执行的详细/简略过程, pytest -v , pytest -q
-k 		指定具体执行哪一个测试用例, 可以是文件名, 也可以是函数名, 都有则需要严格指定py文件名
-x 		测试用例执行失败则立刻停止
-s 		需要执行 print 函数, 默认不执行
-r<option>
  生成简略的指定需求的报告, 支持参数如下

  .. csv-table::
    :header: option, Des

    f, failed
    E, error
    s, skipped
    x, xfailed
    X, passed
    P, passed
    p, passed with output
    a, all except passed
    A, all

  .. +--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
  .. | option             | f                  | E                  | s                  | x                  | X                  | P                  | p                  | a                  | A                  |
  .. +====================+====================+====================+====================+====================+====================+====================+====================+====================+====================+
  .. | Des                | failed             | error              | skipped            | xfailed            | passed             | passed             | passed with output | all except passed  | all                |
  .. +--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+

--tb=<option>

  option: 'auto', 'long', 'short', 'no', 'line', 'native'

  用例运行失败时, 展示错误的详细程度

-l, --showlocals 		用例运行失败时, 打印相关的局部变量, pytest -l
--lf, --last-failed 	只执行上次执行失败的测试
--ff, --failed-first 	先执行完上次失败的测试后, 再执行上次正常的测试
--durations=<num>

  num为0时则倒序显示所有的用例, 为具体值则显示耗时最长的对应该数量的用例, -vv 显示持续时间为0秒的用例

  会按用例执行耗时时长：从长到短 显示结果, 用于调优测试代码

  比如显示运行耗时最长的3个用例且包含持续时间为0秒的：pytest --durations=3 -vv

--maxfail=<num> 	用例运行时 允许的最大失败次数, 超过则立即停止, pytest --maxfail=3
--collect-only 		收集测试用例但不执行
-n<num> 			当使用pytest-xdist插件时, 可以指定运行处理器进程数, 可为个数或者'auto'
--cov=<path> 		统计指定路径的代码测试覆盖率, 需要先安装cov模块: `pip install pytest-cov`
--cov-report=<TYPE>

  生成指定格式的测试报告, 支持多个值, 支持以下测试报告类型: term, term-missing, annotate, html, xml

.. tip:: 运行指定的函数

  pytest 模块名::类名::函数名, pytest test.py::check_ui


.. note::

  代码内部执行

  .. code-block:: python

    if __name__ == '__main__':
      pytest.main()

支持的装饰器
=====================

.. function:: @pytest.mark.run(order=x)

  表示执行顺序

.. function:: @pytest.mark.parametrize('param1, param2', [(param1_data[0], param2_data[0]),(param1_data[1], param2_data[1])])

  存在需要传入多次参数使用

.. function:: @pytest.fixture(name='xxx', scope='function', autouse=False)

  将标记函数设为固件, 直接作为参数使用, name可设置别名, scope设置生效范围, autouse设置是否显示使用

  如果有多个固件, 则会按顺序执行

  scope支持参数:

  - session 	实现多个.py跨文件使用一个session来完成多个用例
  - module 	实现多个.py跨文件共享前置, 每一个.py文件调用一次
  - class		每一个类运行前调用一次
  - function	每一个函数或方法运行前都会调用

  可控制作用范围：session>module>class>function

.. function:: @pytest.mark.skip(reason='xxx')

  跳过测试(如果需要函数内部使用, 直接`pytest.skip(...)`)

.. function:: @pytest.mark.skipif(condition='1>2', reason="xxx")

  含条件判断的跳过

.. function:: @pytest.mark.asyncio

  标记为异步测试函数, 标记后才能正常执行该异步函数

.. function:: @pytest.mark.xfail(reason='xxx')

  标记为预期失败


支持的其他
=====================

- rerunfailure
  失败重跑

  安装, ``pip install pytest-rerunfailure``

  在设置文件pytest.ini中添加命令
  reruns = 重跑次数
  addopts= --reruns =10

  参见: :doc:`/docs/后端/python/python三方库/pytest-rerunfailures`


使用Mock模拟对象
=====================

使用mock对象替代掉指定的python对象, 以达到模拟对象的行为的目的。

可以用在测试时, 存在一些依赖对象时, 使用mock模拟一些依赖对象;

也可以用在存在接口调用但接口未完善时.


.. code-block:: python

  from unittest.mock import Mock

  something = Mock()
  something.do = lambda *args: True

其他见: :doc:`/docs/后端/python/python三方库/pytest`

关于装饰器的一些使用
==========================================

有此节主要是因为, 有需求需要将一个固件重用, 但是变动的地方很小

引入需要用到的模块::

  import pytest
  from _pytest.fixtures import SubRequest
  from _pytest.mark import Mark

定义一个r_server固件, 作用范围为方法域, yield表示会先在yield处返回给测试函数执行直到其结束::

  @pytest.fixture(scope='function')
  def r_server(request: SubRequest):
      print()
      k_kwargs = {k: v for k, v in request.keywords.items()}
      print(
          f'keywords: {k_kwargs}',
            sep='\n')
      yield k_kwargs
      print('end')

其中, request是一个特殊的fixture，它提供了有关当前测试运行上下文的信息.

传递多个普通参数, 给了几组参数就会执行几次当前测试::

  @pytest.mark.parametrize(
      "param1, param2",   # 参数字符串, 注意, 这些参数需要在修饰的方法中定义,
                          # 如此处的 test_r_use_params(param1, param2
      [
          ('p1', 'p2'),   # 第一组参数
          ('p2', 'p3'),   # 第二组参数
          ('p5', 'p4'),   # 第三组参数
                          # 多组参数表示执行多次, 每次使用不同的参数
                          # 这里三组会执行三次, 每次使用本次参数
      ],
      # indirect=['r_server'],  # 要传递的fixture name的list,
                                # 指定哪些个固件使用这些参数
  )
  def test_r_use_params(param1, param2, r_server):
      result: dict = r_server
      assert 'parametrize' in result
      _a: Mark = result['parametrize']
      assert _a.args == ('param1, param2', [('p1', 'p2'), ('p2', 'p3'), ('p5', 'p4')])

这里原本想用 indirect 来指定固件, 不知道为什么使用 indirect 会导致找不到固件而执行失败, 所以放弃.

传递关键字参数::

  # 这里表示传递给 r_server 关键字参数
  # 这里实际传入的是: 'name': Mark(name='name', *args, **kwargs)
  @pytest.mark.key_word_one('1')
  @pytest.mark.key_word_two('2')
  def test_r_use_keywords(r_server):
      result: dict = r_server

      assert 'key_word_one' in result
      assert type(_a := result['key_word_one']) == Mark and _a.args[0] == '1'

      assert 'key_word_two' in result
      assert type(_a := result['key_word_two']) == Mark and _a.args[0] == '2'

可以看出, 不论是关键字参数还是普通参数, 其实都会被 Mark 修饰, 存储到 request.keywords 内.

