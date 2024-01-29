# NJUPT-SAST-WoC
南京邮电大学 - 校大学生科协WoC仓库，用于存放WoC项目。作者 @WiIIiamWei @uiuik0

本仓库仅供讲师浏览。未经允许直接使用/照抄其中代码是不允许且违反WoC规则的。

还在新手村，高手请不要笑我。

**已经完成：所有计算机视觉相关项目。**

**正在进行：网络爬虫（抖音）（项目3）**

## MNIST手写数字识别

模型使用`tensorflow.keras`搭建，结构为CNN。

代码：[NJUPT_WOC-MNIST-fin.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/computer_vision/code/NJUPT_WOC-MNIST-fin.ipynb)

模型：[Releases](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/releases/tag/Submission)

## 猫狗识别

模型使用`keras`搭建，在开源模型[Resnet50](https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5)基础上修改。图片处理使用`rembg`去背景。

### 代码

模型：[catdogde_ww.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/computer_vision/code/catdogde_ww.ipynb)

图片处理（训练集）：[picprocess_train.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/computer_vision/code/picprocess_train.ipynb)

图片处理（测试集）：[picprocess_test.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/computer_vision/code/picprocess_test.ipynb)

图片处理（Alpha通道换白底）：[convert.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/computer_vision/code/convert.ipynb)

### 模型

文件：[Releases](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/releases/tag/Submission)

测试集输出数据：[submission_final.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/computer_vision/data/submission_final.csv)
