========================
DNS劫持
========================

当今互联网流量中，以HTTP／HTTPS为主的Web服务产生的流量占据了绝大部分，
比如抖音、快手、爱奇艺、优酷等等更为突出。Web服务发展如此迅猛，
这背后离不开一个默默无闻的大功臣就是域名解析系统DNS。

如果没有DNS，我们上网需要记忆每个网站的IP地址而不是他们的域名，
这简直是灾难，好在DNS默默在背后做了这一切，我们只需要记住一个域名，剩下的交给DNS来完成吧。

也正是因为其重要性，别有用心的人自然是不会放过它，DNS劫持技术又被发明了出来。

看到这是不是想吐槽一句：怎么什么东西都能当网络攻击手段啊？

没错，所以我们更要了解这些内容，提高自身的防范意识，我们接着说DNS劫持。

DNS提供服务最初是用来将域名转换成IP地址，
然而在早期协议的设计中并没有太多考虑其安全性，所以对于查询方的我们来说会产生诸多疑问：

- 我去请求的真的是一个DNS服务器吗？
- 确定不是别人冒充的？
- 查询的结果有没有被人篡改过？
- 这个IP真是这个网站的吗？

遗憾的是DNS协议中没有机制去保证能回答这些问题，因此DNS劫持现象非常泛滥，
从用户在地址栏输入一个域名的那一刻起，
一路上的凶险防不胜防，好比唐僧独自去西天取经，简直就是小母牛坐电线——牛X带闪电。

后来，为了解决这个问题，出现了DNSSEC技术，
一定程度上可以解决上面的部分问题。但限于一些方面的原因，
这项技术并没有大规模使用，尤其在国内，鲜有部署应用。

再后来，以阿里、腾讯等头部互联网厂商为首开始推出了httpDNS服务，
来了一招釜底抽薪，虽然这项技术的名字中还有DNS三个字母，
但实现上和原来但DNS已经是天差地别，
通过这项技术让DNS变成了在http协议之上的一个应用服务。
所以现在国内网站基本很少会遇到DNS劫持的事件。




