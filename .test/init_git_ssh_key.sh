#! /bin/bash

###
# 此脚本用于生产gitee需要的公钥并部署
###

sky_blue_echo(){
	local _strs
	_strs="$*"
	printf "\e[1;36m%s\e[0m\n" "${_strs}"
}

y_echo(){
	local _strs
	_strs="$*"

	# echo "####-stdout-#### ${_strs}"
	sky_blue_echo "####-stdout-#### ${_strs}"
}

# 注意：这里的 xxxxx@xxxxx.com 只是生成的 sshkey 的名称，并不约束或要求具体命名为某个邮箱。
# 现网的大部分教程均讲解的使用邮箱生成，其一开始的初衷仅仅是为了便于辨识所以使用了邮箱。
y_echo "开始生产密钥, 请根据提示进行操作"
ssh-keygen -t ed25519 -C "yanquer@qq.com"
# Generating public/private ed25519 key pair...

# 按照提示完成三次回车，即可生成 ssh key。

# 通过查看 ~/.ssh/id_ed25519.pub 文件内容，获取到你的 public key
y_echo "生成的公钥为: "
cat ~/.ssh/id_ed25519.pub

# 复制生成后的 ssh key，通过仓库主页 「管理」->「部署公钥管理」->「添加部署公钥」 ，添加生成的 public key 添加到仓库中。
y_echo "请复制生成后的 ssh key，通过仓库主页 「管理」->「部署公钥管理」->「添加部署公钥」 ，添加生成的 public key 添加到仓库中。"

open 'https://gitee.com/profile/sshkeys'

tip='n'

while [ "${tip}" != 'y' ]; do
	read -p "添加成功后输入 y 确认 >" -r tip
done

y_echo "开始测试gitee的链接..."
# ssh -T git@gitee.com

if ssh -T git@gitee.com; then
	y_echo "链接成功"
else
	y_echo "链接失败"
fi
