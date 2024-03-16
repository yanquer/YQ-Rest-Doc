
===========================
dialog更新父组件数据域
===========================

.. post:: 2023-03-01 00:19:35
  :tags: 框架, amis, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn

一般来说有两种方案

方案一:
  如果使用的是API, 在dialog上增加一个数据更新的API即可,
  外部也需要有查询的API
方案二:
  使用dialog提供的 ``setValue``, 可以指定更新某位置的数据域,
  需要提前使用id指定位置::

    {
        type: "service",
        data: {
            envData: this.state._envData,
            eName: 'tt'
        },
        body: [
            {
                type: 'grid',
                columns: [
                    {
                        type: 'form',
                        id: 'top-form',
                        body: [
                            {
                                type: 'input-text',
                                name: 'eName',
                                label: 'label0',
                                mode: "horizontal",
                            },
                            {
                                type: 'flex',
                                style: {
                                    width: '100%',
                                    height: '100%',
                                    justifyContext: 'flex-end',
                                    flexDirection: 'column'
                                },
                                items: [
                                    {
                                        icon: 'fas fa-list-ul',
                                        type: 'button',
                                        actionType: 'dialog',
                                        dialog: {
                                            type: 'dialog',
                                            body: [
                                                {
                                                    type: "input-kv",
                                                    name: "envData",
                                                },
                                                {
                                                    type: 'input-text',
                                                    label: "name${eName}",
                                                    name: 'eName',
                                                }
                                            ],
                                            onEvent: {
                                                confirm: {
                                                    actions: [
                                                        {
                                                            actionType: 'setValue',
                                                            componentId: "top-form",
                                                            args: {
                                                                value: {
                                                                    eName: 'x${eName}'
                                                                }
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                        }
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
        ]
    },

  主要的, 定义id::

    id: 'top-form',

  定义执行更新时候的数据::

    onEvent: {
        confirm: {
            actions: [
                {
                    actionType: 'setValue',
                    componentId: "top-form",
                    args: {
                        value: {
                            eName: 'x${eName}'
                        }
                    }
                }
            ]
        }
    }

  注意, 貌似只能更新某一条数据链上的内容

  默认setValue会将新数据与目标组件数据进行合并;
  可以通过"dataMergeMode": "override"来覆盖目标组件数据;

  **除非是当前数据链上的数据, 否则需要指定额外的id去更新指定控件的数据**



