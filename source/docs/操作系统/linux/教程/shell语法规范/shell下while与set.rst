============================
shell下while与set
============================

使用了::

    set -e

时, 一定要注意不能包裹 while 语句.

while语句的最后一次结果, 会返回1, 退出while循环, 然后set -e就会觉得是代码报错了, 不给后续代码执行

例::

    set -e

    blue_echo(){
        local _strs
        _strs="$*"

        echo "\e[1;36m${_strs}\e[0m\n"
    }

    pv_blue_echo(){
        local _time
        _time="$1"

        set +e

        while [ ${_time} -gt 0 ]; do

            blue_echo "................" | pv -qL 15
            _time="$(expr "${_time}" - 1)"
        done

        set -e
    }

    # pv_blue_echo 3


