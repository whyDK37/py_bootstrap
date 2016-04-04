#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    把gradle 下载的仓库转化为maven仓库的目录结构
    gradle 的仓库默认下载到用户目录下，如：C:\\Users\\whydk[user name]\\.gradle\\caches\\modules-2\\files-2.1
    gradle 仓库的目录结构是：groupId/artifactId/version/sha1/pom,jar
            如：org.apache.tiles\\tiles-api\\3.0.4\83940300a42975f32339e2190acd7d326c3b642d\\tiles-api-3.0.4.pom
    maven  仓库的目录结构是：groupId[按.分隔目录]/artifactId/version/pom,jar,sha1
            如：org\\apache\\tiles\\tiles-api\\3.0.4\\tiles-api-3.0.4.pom
                org\\apache\\tiles\\tiles-api\\3.0.4\\tiles-api-3.0.4.pom.sha1(内容为83940300a42975f32339e2190acd7d326c3b642d)
"""
import os,shutil

userhome = os.path.expanduser('~')
gradle_repo_root = userhome+"/.gradle/caches/modules-2/files-2.1"
maven_repo_root = "D:/OneDrive/.m2/repository"

def trans_gradle_maven(groupId):
    mvngroupId = "";
    forlder_arr = groupId.split(".")
    if (len(forlder_arr) != 1):
        for index in range(len(forlder_arr)):
            mvngroupId += forlder_arr[index] + "/";
    else:
        mvngroupId = forlder_arr[0]
    print("maven 仓库目录", maven_repo_root + "/" + mvngroupId)
    mkdirifnotexist(maven_repo_root + "/" + mvngroupId)

    artifactIds = os.listdir(gradle_repo_root + "/" + groupId)
    # 复制gradle仓库
    for index in range(len(artifactIds)):
        artifactId = artifactIds[index];
        versions = os.listdir(gradle_repo_root + "/" + groupId + "/" + artifactId)
        # 模块
        for index in range(len(versions)):
            version = versions[index];
            #groupId  artifactId version
            gav = gradle_repo_root + "/" + groupId + "/" + artifactId + "/" + version
            sha1s = os.listdir(gav)
            # 版本,下分目录存放jar,pom,source
            for index in range(len(sha1s)):
                sha1 = sha1s[index]
                filename = os.listdir(gav + "/" + sha1)[0];
                ##复制到maven仓库
                mkdirifnotexist(
                    maven_repo_root + "/" + mvngroupId + "/" + artifactId + "/" + version)
                shutil.copy(gav + "/" + sha1 + "/" + filename,
                            maven_repo_root + "/" + mvngroupId + "/" + artifactId + "/" + version + "/" + filename)
                #创建 SHA1 文件
                fileHandle = open ( maven_repo_root + "/" + mvngroupId + "/" + artifactId + "/" + version + "/" + filename+".sha1", 'w' )
                fileHandle.write ( sha1 )
                fileHandle.close()
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

groupIds = os.listdir(gradle_repo_root)
for index in range(len(groupIds)):
    groupId = groupIds[index];
    print("仓库：", groupId)
    trans_gradle_maven(groupId)


