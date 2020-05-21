

apt





目录
--

1.  1 [简介](#1)
2.  2 [工作原理](#2)
3.  3 [常用命令](#3)

<a name="1" class="lemma-anchor para-title"></a><a name="sub20826172_1" class="lemma-anchor "></a><a name="简介" class="lemma-anchor "></a>

apt简介
-----

[编辑](javascript:;)Advanced Packaging Tool（apt）是Linux下的一款安装包[管理工具](/item/%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7)。最初只有.tar.gz的打包文件，用户必须编译每个他想在GNU/Linux上运行的软件。用户们普遍认为系统很有必要提供一种方法来管理这些安装在机器上的软件包，当Debian诞生时，这样一个管理工具也就应运而生，它被命名为dpkg。从而著名的"package"概念第一次出现在GNU/Linux系统中，稍后Red Hat才决定开发自己的"rpm"包管理系统。很快一个新的问题难倒了GNU/Linux制作者，他们需要一个快速、实用、高效的方法来安装软件包，当软件包更新时，这个工具应该能自动管理关联文件和维护已有配置文件。Debian再次率先解决了这个问题，APT(Advanced Packaging Tool）作为dpkg的前端诞生了。APT后来还被Conectiva改造用来管理rpm，并被其它Linux发行版本采用为它们的软件包[管理工具](/item/%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7)。APT由几个名字以"apt-"打头的程序组成。[apt-get](/item/apt-get)、apt-cache 和apt-cdrom是处理软件包的命令行工具。Linux命令---apt，也是其它用户前台程序的后端，如dselect 和[aptitude](/item/aptitude)。作为操作的一部分，APT使用一个文件列出可获得软件包的镜像站点地址，这个文件就是/etc/apt/sources.list。<a name="2" class="lemma-anchor para-title"></a><a name="sub20826172_2" class="lemma-anchor "></a><a name="工作原理" class="lemma-anchor "></a>

apt工作原理
-------

[编辑](javascript:;)APT是一个客户/[服务器系统](/item/%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%B3%BB%E7%BB%9F)。在服务器上先复制所有DEB包（DEB是Debian软件包格式的[文件扩展名](/item/%E6%96%87%E4%BB%B6%E6%89%A9%E5%B1%95%E5%90%8D)），然后用APT的分析工具（genbasedir）根据每个DEB 包的包头（Header）信息对所有的DEB包进行分析，并将该分析结果记录在一个文件中，这个文件称为DEB 索引清单，APT服务器的DEB索引清单置于base文件夹内。一旦APT 服务器内的DEB有所变动，一定要使用genbasedir产生新的DEB索引清单。客户端在进行安装或升级时先要查询DEB索引清单，从而可以获知所有具有依赖关系的软件包，并一同下载到客户端以便安装。当客户端需要安装、升级或删除某个软件包时，客户端计算机取得DEB索引清单压缩文件后，会将其解压置放于/var/state/apt/lists/，而客户端使用[apt-get](/item/apt-get) install或apt-get upgrade命令的时候，就会将这个文件夹内的数据��客户端计算机内的DEB数据库比对，知道哪些DEB已安装、未安装或是可以升级的。<a name="3" class="lemma-anchor para-title"></a><a name="sub20826172_3" class="lemma-anchor "></a><a name="常用命令" class="lemma-anchor "></a>

apt常用命令
-------
- apt-cache search # ——（package 搜索包）
- apt-cache show #——（package 获取包的相关信息，如说明、大小、版本等）
- sudo apt-get install # ——（package 安装包）
- sudo apt-get reinstall # —–（package - - reinstall 重新安装包）
- sudo apt-get -f install # —–（强制安装?#”-f = –fix-missing”当是修复安装吧…）
- sudo apt-get remove #—–（package 删除包）
- sudo apt-get remove --purge # ——（package 删除包，包括删除配置文件等）
- sudo apt-get autoremove --purge # —-(package 删除包及其依赖的软件包配置文件等（只对6.10有效，强烈推荐））
- sudo apt-get update #——更新源
- sudo apt-get upgrade #——更新已安装的包
- sudo apt-get dist-upgrade # ———升级系统
- sudo apt-get dselect-upgrade #——使用 dselect 升级
- apt-cache depends #——-(package 了解使用依赖）
- apt-cache rdepends # ——（package 了解某个具体的依赖?#当是查看该包被哪些包依赖吧…）
- sudo apt-get build-dep # ——（package 安装相关的编译环境）
- apt-get source #——（package 下载该包的源代码)
- sudo apt-get clean && sudo apt-get autoclean # ——–清理下载文件的存档 && 只清理过时的包
- sudo apt-get check #——-检查是否有损坏的依赖
- apt-get install# ——（下载 以及所有依赖的包裹，同时进行包裹的安装或升级。如果某个包裹被设置了 hold （停止标志，就会被搁在一边（即不会被升级）。更多 hold 细节请看下面。）
- apt-get remove [--purge]# ——（移除 以及任何倚赖这个包裹的其它包裹。）
- --purge 指明这个包裹应该被完全清除 (purged) ，更多信息请看 dpkg -P。
- apt-get update# ——（升级来自 Debian 镜像的包裹列表，如果你想安装当天的任何软件，至少每天运行一次，而且每次修改了/etc/- apt/sources.list 后，必须执行。）
- apt-get upgrade [-u]# ——（升级所有已经安装的包裹为最新可用版本。不会安装新的或移除老的包裹。形前端（其中一些在使用前得先安装）。这里 dselect 无疑是最强大的，也是最古老，最难驾驭。）
