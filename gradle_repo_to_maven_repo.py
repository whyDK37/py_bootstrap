#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    把gradle 下载的仓库转化为maven仓库的目录结构
    gradle 的仓库默认下载到用户目录下，如：C:\\Users\\whydk\\.gradle\\caches\\modules-2\\files-2.1
"""
import os,shutil

gradle_repo_root = "C:\\Users\\whydk\\.gradle\\caches\\modules-2\\files-2.1"
maven_repo_root = "D:\\mrp"

def trans_gradle_maven(gradle_lib):
    maven_lib = "";
    forlder_arr = gradle_lib.split(".")
    if (len(forlder_arr) != 1):
        for index in range(len(forlder_arr)):
            maven_lib += forlder_arr[index] + "\\";
    else:
        maven_lib = forlder_arr[0]
    print("maven 仓库目录", maven_repo_root + "\\" + maven_lib)
    mkdirifnotexist(maven_repo_root + "\\" + maven_lib)

    gradlelibs = os.listdir(gradle_repo_root + "\\" + gradle_lib)
    # 复制gradle仓库
    for index in range(len(gradlelibs)):
        gradlelibmodel = gradlelibs[index];
        gradlemodels = os.listdir(gradle_repo_root + "\\" + gradle_lib + "\\" + gradlelibmodel)
        # 模块
        for index in range(len(gradlemodels)):
            gradlelibmodelversion = gradlemodels[index];
            gradlejar = gradle_repo_root + "\\" + gradle_lib + "\\" + gradlelibmodel + "\\" + gradlelibmodelversion
            gradlejars = os.listdir(gradlejar)
            # 版本,下分目录存放jar,pom,source
            for index in range(len(gradlejars)):
                filename = os.listdir(gradlejar + "\\" + gradlejars[index])[0];
                ##复制到maven仓库
                mkdirifnotexist(
                    maven_repo_root + "\\" + maven_lib + "\\" + gradlelibmodel + "\\" + gradlelibmodelversion)
                shutil.copy(gradlejar + "\\" + gradlejars[index] + "\\" + filename,
                            maven_repo_root + "\\" + maven_lib + "\\" + gradlelibmodel + "\\" + gradlelibmodelversion + "\\" + filename)
    return


def mkdirifnotexist(path):
    if (os.path.exists(path)):
        pass
    else:
        os.makedirs(path)


# str ="ab"
# print(str.split("."))
# print(len(str.split(".")))
# print(os.path.dirname(gradle_repo_path))
# print(os.listdir(gradle_repo_path));

if (os.path.exists(gradle_repo_root)):
    print("gradle 仓库目录为：", gradle_repo_root)
else:
    print("gradle 仓库目录不存在：", gradle_repo_root)
    exit();

if (os.path.exists(maven_repo_root)):
    print("maven仓库临时目录：", maven_repo_root)
else:
    os.mkdir(maven_repo_root)
    print("创建maven仓库临时目录：", maven_repo_root)

gradlelibs = os.listdir(gradle_repo_root)
for index in range(len(gradlelibs)):
    gradle_lib = gradlelibs[index];
    print("仓库：", gradle_lib)
    trans_gradle_maven(gradle_lib)
    # if index == 10 :
    #     break

print()
print("请把",maven_repo_root,"目录的文件拷贝到maven主仓库。")