========================================
string.h
========================================


.. post:: 2023-02-20 22:06:49
  :tags: c, 标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


.. _Cstring_strcpy:

strcpy
========================================

strcpy(a, b):
  相当于python的值传递赋值, 把b复制一份给a

strcat
========================================

strcat(a, b):
  字符串原地拼接, 相当于python的 `a = a+b`

strlen
========================================

.. function:: size_t strlen(const char *str)

  获取字符串长度

strtok
========================================

.. function:: char *strtok(char *s, const char *delim);

  字符串分割函数

  s是指向要分割的字符串的指针，delim是包含分隔符字符的字符串;
  线程不安全的，如果需要在多线程环境中使用,
  应当使用strtok_r函数或者其他线程安全的替代函数

  会同步修改原有字符串s.

  将一个字符串拆分成多个子字符串, 需要进行多次字符串拆分时,
  第一次调用时传入原始字符串，并在后续的调用中传入 NULL 作为第一个参数::

    char str[] = "it is test!";
    char *token;

    // 使用空格作为分隔符
    token = strtok(str, " ");

    // 后续用NULL即可
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, " ");
    }

  这是因为 strtok 函数会在原始字符串上插入空字符（\0）来截断子字符串.
  第一次调用时，它会从原始字符串开始处理，并返回第一个子字符串的指针;
  后续传入 NULL 作为第一个参数, 告诉 strtok 函数继续从上一次截断的位置开始处理，并返回下一个子字符串的指针
  (必须保证原始字符串是可修改的)

  .. note::

    特别要注意分割处理后原字符串 str 会变，变成第一个子字符串, 分割字符会被替换为 "\0"::

      #include <string.h>
      #include <stdio.h>

      int main()
      {
          char str[80] = "This is - www.runoob.com - website";
          const char s[2] = "-";
          char *token;

          /* 获取第一个子字符串 */
          token = strtok(str, s);

          /* 继续获取其他的子字符串 */
          while (token != NULL)
          {
              printf("%s\n", token);

              token = strtok(NULL, s);
          }
          printf("\n");
          for (int i = 0; i < 34;i++)
              printf("%c", str[i]);

          return (0);
      }

    输出::

      This is
        www.runoob.com
        website

      This is  www.runoob.com  website






