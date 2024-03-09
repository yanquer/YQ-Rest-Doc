========================
lodash
========================

节流与消抖
  节流(throttle): n 秒内只运行一次，若在 n 秒内重复触发，只有一次生效

  消抖(debounce): n 秒后在执行该事件，若在 n 秒内被重复触发，则重新计时

  参考: `https://vue3js.cn/interview/JavaScript/debounce_throttle.html#代码实现`

.. important::

  此库提供的节流与消抖, 是一个回调而不是函数调用.

  类似于::

    const Sleep = (ms: number)=> {
      return new Promise(resolve=>setTimeout(resolve, ms))
    }

    const debounce = async (func, wait: number) => {
      if (typeof func !== 'function') {
        throw new TypeError('Expected a function')
      }

      // 等待 xxx ms
      await Sleep(wait);
      return func
    }

  这里的代码其实有点问题, 没有实现到 ``重复触发，重新计时``


lodash用于节流(throttle)函数的调用频率,以提高性能。

限制指定的时间间隔内最多执行一次原函数。也就是说,它限制了调用函数的频率,避免函数被过于频繁地调用。

使用 lodash.throttle 的好处有:

- 防止频繁的事件触发导致性能问题,如 resize、scroll 等事件的处理函数。
- 控制动画或轮询功能的频率,避免过度占用 CPU 资源。
- 网络请求频率控制,减少不必要的请求量。
- 输入框实时搜索suggestions时限制请求频率。

例如::

  import { throttle } from 'lodash';

  function handleResize() {
    // 处理窗口 resize
  }

  window.addEventListener('resize', throttle(handleResize, 100));

这将限制 handleResize 函数每 100ms 至多执行一次,从而提高页面滚动时的性能。



