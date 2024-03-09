=================================
Mac-Vmware磁盘修复
=================================

Mac下面个人免费的虚拟机好像只有Vmware的
`Vmware Fusion`, 有时候由于磁盘空间不足啊等原因可能会
造成 **指定的虚拟磁盘需要修复**

这个时候好像重启Vmware就可以修复.

若不行::

  cd /Applications/VMware\ Fusion.app/Contents/Library/
  ./vmware-vdiskmanager -R "/Users/yanque/Virtual Machines.localized/Ubuntu 64 位 14.04.6.vmwarevm/虚拟磁盘.vmdk"





