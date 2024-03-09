==================================
一些XML配置属性
==================================

screenOrientation
----------------------------------

Android应用程序中， **android:screenOrientation**
用于 **控制activity启动时方向**，也就是横竖屏展示。

下面列出常用的属性值：

• unspecified，默认值，由系统决定，不同手机可能不一致
• landscape，强制横屏显示
• portrait，强制竖屏显示
• behind，与前一个activity方向相同
• sensor，根据物理传感器方向转动，用户90度、180度、270度旋转手机方向，activity都更着变化
• sensorLandscape，横屏旋转，一般横屏游戏会这样设置
• sensorPortrait，竖屏旋转
• nosensor，旋转设备时候，界面不会跟着旋转。初始化界面方向由系统控制
• user，用户当前设置的方向
• fullSensor 显示的方向（4个方向）是由设备的方向传感器来决定的，
  除了它允许屏幕有4个显示方向之外，其他与设置为“sensor”时情况类似，
  不管什么样的设备，通常都会这么做。
  例如，某些设备通常不使用纵向倒转或横向反转，但是使用这个设置，
  还是会发生这样的反转。这个值在API Level 9中引入
• fulluser 如果用户锁定了基于传感器的旋转，其行为与 user 相同，
  否则，其行为与 fullSensor 相同，允许所有4种可能的屏幕方
  向。API级别 18中的新增配置。
• locked 将方向锁定在其当前的任意旋转方向。API级别 18 中的新增配置。

参考: `<https://blog.csdn.net/lixiaoliang0723/article/details/105220692>`_


