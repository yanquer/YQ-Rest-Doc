===============
readme
===============

说明
===============

- 文档都放在 ``source/docs`` 目录下
- generate是生成 ``toctree`` 结构的, yaml 是相关配置文件

    执行 main.py 即可

    yaml 配置

    - doc_index_rst_path: source/index.rst

        index 文件位置, 文档树会写进这里面

    - doc_dir: source/docs

        文档位置

    - exclude_dir: ['resources']

        需要排除的目录

- ``make html`` 编译

.. note::

    文档编码说明, 会自动扫描 *docs* 下所有文件夹, 可参考上面说明配置.

    如果文件夹下还存在子文件树, 则需手动在目录下配置 *index.rst* 文件, 生成会自动识别此文件作出相应更新

运行
===============

docker运行::

    docker run --name mynginx -v /Users/yanque/project/new_doc_rst/build/html:/usr/share/nginx/html -p 80:80 -d nginx

关于主题
===============

当前主题使用是基于 sphinx5.3.0 的, 如果更新会有样式问题, 之前更新了一次导致构建样式出问题.
后面干脆把正常的样式的包全部freeze到了 rst_package.txt 里面, 不正常的在rst_package_311.txt.
粗略对比了一下就是sphinx版本问题, 没有细测, 太费时间.

若还有其他包, 找个虚拟环境::

    pip install -r rst_package.txt

即可.

迁移历史
===============

从md文档迁移当current

此前已完成
    redis
    python

24.2.5
    nginx, mysql迁移完成

    elasticsearch 迁移完成

django, AI, 计算机网络 相关迁移完成

python 迁移完成, 多进程部分待完全整理...



