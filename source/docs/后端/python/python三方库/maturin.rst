=====================================
maturin
=====================================

将 `Rust` 代码编译为Python包

安装::

  pip install maturin

Python包生成
=====================================

先进入 `项目根目录`, 然后执行::

  maturin init

会生成 `Cargo.toml` 和 `lib.rs`

然后::

  maturin develop

如果之前没配置过Rust， 参考 :doc:`/docs/后端/rust/index`



