===========================
theia启动白屏
===========================

可以从官方仓库的提交记录中发现端倪: `https://github.com/eclipse-theia/theia/commit/45a0953d7eed19cd311840281f17999d268ba7cf` ,
但, 其实对没有配置 `preloadTemplate` 的项目影响不大,
但是如果配置了, 那启动时, 会很早就打开一个初始化窗口, 且这个时候只能用给的默认的背景色,
不过可以通过配置 ``"showWindowEarly": false`` 来不启动这个早期窗口,
暂时这样解决吧::

    "theia": {
        "target": "electron",
        "frontend": {
        "config": {
            "applicationName": "Theia Electron Example",
            "electron": {
            "showWindowEarly": false
            }
        }
        },
        "generator": {
        "config": {
            "preloadTemplate": "./resources/preload.html"
        }
        }
    },
