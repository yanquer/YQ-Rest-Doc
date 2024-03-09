=================================================
在theia的react-dialog上新增自定义dialog
=================================================

使用开发者工具可以看出,
theia内置的react-dialog是先覆盖了一层 `z-index` 为 5000 的 `div`:

.. figure:: ../../../../../resources/images/2023-11-15-10-14-50.png
  :width: 480

.. note::

  这里的 `react-dialog` 即::

    import {ReactDialog} from "@theia/core/lib/browser/dialogs/react-dialog";

如果要在其上再弹出一个dialog, 要么, 减小原有的这个 5000; 要么, 增大需要增加的 `z-index`

