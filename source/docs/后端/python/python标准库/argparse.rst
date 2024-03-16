=================
argparse
=================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


基本使用模板::

  # 导入argparse
  import argparse

  parser = argparse.ArgumentParser(description="Demo of argparse")  # 生成argparse对象
  parser.add_argument('-n','--name', default=' Li ')          # 增加参数
  args = parser.parse_args()                                  # 获取


add_argument参数列表::

  default         # add_argument
  required        # 这个参数是否一定需要设置
  type            # 参数类型
  choices         # 参数值只能从几个选项里面选择
  help            # 指定参数的说明信息
  dest            # 设置参数在代码中的变量名

  nargs           # 设置参数在使用可以提供的个数
            # 值      含义
               N    # 参数的绝对个数（例如：3）
              '?'   # 0或1个参数
              '*'   # 0或所有参数
              '+'   # 所有，并且至少一个参数

例::

  parser.add_argument('-n', defalut=1, required=True, type=int, choices=[1,2,3], help='is number', dest=iNum, nargs='?')

例子::

  import argparse

  def main():
      parser = argparse.ArgumentParser(description="Demo of argparse")
      parser.add_argument('-n','--name', default=' Li ')
      parser.add_argument('-y','--year', default='20')
      args = parser.parse_args()
      print(args)
      name = args.name
      year = args.year
      print('Hello {}  {}'.format(name,year))

  if __name__ == '__main__':
      main()






