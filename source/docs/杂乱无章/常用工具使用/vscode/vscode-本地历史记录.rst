======================================
vscode-本地历史记录
======================================


.. post:: 2024-03-09 18:21:01
  :tags: vscode
  :category: 常用工具使用
  :author: YanQue
  :location: CD
  :language: zh-cn


vscode编辑器内置了本地文件历史记录的支持, 可以通过配置setting.json自定义,
默认的配置如下::

  // 控制是否启用本地文件历史记录。启用后，所保存编辑器文件内容将存储到备份位置，以便稍后可以还原或查看内容。更改此设置不会影响现有本地文件历史记录条目。
	"workbench.localHistory.enabled": true,

	// 配置路径或 [glob 模式](https://aka.ms/vscode-glob-patterns)以排除本地文件历史记录中的文件。glob 模式的计算结果始终是相对于工作区文件夹路径所在的位置，除非它们是绝对路径。更改此设置不会影响现有的本地文件历史记录条目。
	"workbench.localHistory.exclude": {},

	// 控制每个文件的最大本地文件历史记录条目数。当文件的本地文件历史记录条目数超过此数目时，将丢弃最早的条目。
	"workbench.localHistory.maxFileEntries": 50,

	// 控制考虑用于本地历史记录的文件最大大小(KB)。较大的文件将不会添加到本地历史记录中。更改此设置不会影响现有本地文件历史记录条目。
	"workbench.localHistory.maxFileSize": 256,

	// 配置时间间隔(以秒为单位)，在此间隔期间，本地文件历史记录中的最后一个条目将替换为正在添加的条目。这有助于减少所添加的条目总数，例如启用自动保存时。此设置仅应用于具有相同源的条目。更改此设置不会影响现有本地文件历史记录条目。
	"workbench.localHistory.mergeWindow": 10,

源码相关
======================================

历史文件是全拷贝到一个临时位置,
临时位置跟据用户机器, 一般Windows默认是 `$APPDATA/Roaming/Code/User/History`

下面的每一个文件夹都是16进制的 源文件全路径的hash值(即每一个文件夹对应一个实际的文件),
下面的每个条目表示每一次的记录全拷贝, 命名为: 四位随机数+后缀

对应关系在条目文件夹的 `entries.json` 内.

服务源码位置: `src/vs/workbench/services/workingCopy/common/workingCopyHistoryService.ts`





