# NJUPT-SAST-WoC-2023-Python

南京邮电大学 - 校大学生科协WoC仓库（2023~2024 Python组任务），用于存放WoC项目。作者 @WiIIiamWei @uiuik0

~~本仓库仅供讲师浏览。未经允许直接使用/照抄其中代码是不允许且违反WoC规则的。~~

本项目正式结项。项目可见性将从私人转为公开。

还在新手村，高手请不要笑我。

### 现在的状态

所有项目已基本完成，可以验收，有空会改进。

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

测试集输出数据：[submission_final.csv](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/computer_vision/data/submission_final.csv)

## 爬取抖音

已基本实现所有要求的功能。

代码：[tiktok_2.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/web_crawler/code/tiktok_2.ipynb)

爬取数据（为方便浏览，改成了csv）：[抖音热搜榜.csv](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/web_crawler/data/抖音热搜榜.csv)

## 爬取淘宝评论

项目已经成功爬取至少365条评论，运行 ~~还算稳定（需要fresh cookies）~~ 不太稳定，在不同环境上表现不同。

正确爬取的数据嵌入在爬取代码中。

### 代码

从淘宝搜索页提取的XHR文件提取商品id：[get_id.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/web_crawler/code/get_id.ipynb)

提取登录cookies：[get_cookies.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/web_crawler/code/get_cookies.ipynb)

爬取：[tb.ipynb](https://github.com/WiIIiamWei/NJUPT-SAST-WoC/blob/main/web_crawler/code/tb.ipynb)
