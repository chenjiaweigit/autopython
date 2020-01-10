# coding: utf-8
import shutil
import zipfile
import tarfile

#shutil 对压缩包的处理是通过调用zipfile 和 TarFile两个模块来进行的。
#shutil则就是对os中文件操作的补充。--移动 复制  打包 压缩 解压
if __name__ == '__main__':
    # shutil.copyfile(r'E:\banben.txt',r'E:\banben2.txt')#复制
    # shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
    # shutil.copytree('f1', 'f2', symlinks=True, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))#递归拷贝
    # shutil.move('folder1', 'folder3')#递归移动
    # 压缩
    z = zipfile.ZipFile('laxi.zip', 'w')
    z.write('a.log')
    z.write('data.data')
    z.close()

    # 解压
    z = zipfile.ZipFile('laxi.zip', 'r')
    z.extractall()
    z.close()
    # # 压缩
    # tar = tarfile.open('your.tar', 'w')
    # tar.add('/Users/wupeiqi/PycharmProjects/bbs2.log', arcname='bbs2.log')
    # tar.add('/Users/wupeiqi/PycharmProjects/cmdb.log', arcname='cmdb.log')
    # tar.close()
    #
    # # 解压
    # tar = tarfile.open('your.tar', 'r')
    # tar.extractall()  # 可设置解压地址
    # tar.close()
