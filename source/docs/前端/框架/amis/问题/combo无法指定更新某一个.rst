
===========================
combo无法指定更新某一个
===========================

第一次遇到是使用 `input-array` ,
数组的每一个项有多个指定的值,

指定项id并使用 `componentId` , 会造成只能更新第一个项的数据,
即使是由其他项触发.

这个时候可以使用 `componentName` 指定当前项的name, 会自动处理

实测使用官网提的 `this.index` 无效: `https://aisuda.bce.baidu.com/amis/zh-CN/components/form/combo#设置序号`


