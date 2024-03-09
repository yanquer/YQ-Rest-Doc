=============================
chrome支持的选项
=============================

从指定位置启动浏览器(即Chrome执行文件路径),
binary 参数接收一个使用浏览器的备用路径,
通过这个参数你可以使用chromedriver 去驱动各种基于Chromium 内核的浏览器.::

  options.binary_location = chrome_bin

增加插件::

  options.add_extension(extension_file_path)

保持浏览器的打开状态
将 detach 参数设置为true将在驱动过程结束后保持浏览器的打开状态::

  options.add_experimental_option("detach", True)

排除的参数,
Chrome 添加了各种参数，如果你不希望添加某些参数，
可以将其传入 excludeSwitches. 一个常见的例子是重新打开弹出窗口阻止程序.::

  options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

指定日志输出::

  service = webdriver.ChromeService(log_output=log_path)

指定控制台输出::

  service = webdriver.ChromeService(log_output=subprocess.STDOUT)

指定日志等级::

  service = webdriver.ChromeService(service_args=['--log-level=DEBUG'], log_output=subprocess.STDOUT)

指定日志效果(支持 `append log` 和 `readable timestamps`)::

  service = webdriver.ChromeService(service_args=['--append-log', '--readable-timestamp'], log_output=log_path)

禁用版本检查,
默认会检查驱动与浏览器的版本是否一致::

  service = webdriver.ChromeService(service_args=['--disable-build-check'], log_output=subprocess.STDOUT)

