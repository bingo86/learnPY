编译安装git
1.安装git所需要调用和依赖的代码库
yum install curl-devel expat-devel gettext-devel \
  openssl-devel zlib-devel perl-ExtUtils-MakeMaker
2.下载git最新代码
	http://git-scm.com/download
3.解压
	tar -zxf git-VERSION.tar.gz
4.编译
	make prefix=/usr/local all
5.安装
	sudo make prefix=/usr/local install

