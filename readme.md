<center>实验室人脸识别开门系统</center>

### 简介
实验室使用的门是电磁吸门，每次开门需要输入密码，因为之前图像处理课曾经学过人脸识别，因此想到使用树莓派接摄像头完成人脸识别，然后控制舵机按下室内的开门按钮，实验人脸识别并自动开门
### 主要硬件

树莓派+usb摄像头+舵机开关

### 主要思想

刚开始想用树莓派直接进行人脸识别，但是后来发现树莓派的性能太差，在处理人脸特征信息时卡的严重，因此想到了使用远程识别的思路。
具体思路：
树莓派连接摄像头，通过mjpg-stream，将摄像头信息传输给远程服务器，远程服务器对图像进行处理，当识别实验室的人像时，使用socket给树莓派传输开门命令，树莓派接收到指令后控制舵机开门。

### 人脸识别

人脸识别程序由于自己写的算法精确度较低，因此使用了网上一个大佬的算法，在此想该同学表示感谢，源码地址：
https://github.com/coneypo/Dlib_face_recognition_from_camera

本文只有控制舵机的代码，人脸识别算法可看上面同学的代码
Communication文件夹为测试代码
control文件夹中是舵机控制代码，也就是树莓派中执行的脚本核心代码

videos文件夹中是演示视频

### 语音识别
加入语音模块，实现语音控制开门
