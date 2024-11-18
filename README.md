# 蚊子识别以及计数工具

## 介绍
本项目为一个基于深度学习，以识别蚊子和统计蚊子数量为目的的系统。该系统的核心深度学习模型基于YOLO v8预训练模型，通过自定义数据集训练得到，可检测到图像中的蚊子，进而输出蚊子数量。

## 环境设置及安装
- 请确保运行环境中安装好Python（3.8及以上），并设置好pip。推荐使用Anaconda来管理Python虚拟环境。
- 请参考[Python官方文档](https://www.python.org/downloads/)进行Python的安装。
- 如果使用Anaconda，请参考[Anaconda官方安装指南](https://docs.anaconda.com/anaconda/install/)
    - 安装完成Anaconda后，运行如下命令来启动一个新的虚拟环境：
    ```bash
    conda create --name mosquito-inference python=3.8
    conda activate mosquito-inference
    ```
- 安装所需的包：
    - ```pip install -r requirements.txt```

## 运行
- 将需要处理的图片放到```images```文件夹下，如果是计数任务，只能放一张图片，如果是检测任务，可以放多张图片及视频。
- 计算蚊子个数
    - Mac及Linux：运行```python count/count.py```
    - Windows： 运行```python count\count.py```
    - 结果会显示在命令行中
- 检测图片中的蚊子：
    - Mac及Linux：运行```python detect/detect.py```
    - Windows： 运行```python detect\detect.py```
    - 运行完成后在```output```目录下查看结果

