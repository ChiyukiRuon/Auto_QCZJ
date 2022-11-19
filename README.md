# Auto_QCZJ
适用于云函数部署的青年大学习自动打卡，**仅限浙江地区使用**  
原项目地址[WuliAPO/Fuck_QCZJ](https://github.com/WuliAPO/Fuck_QCZJ)

## 功能
* 可用于多用户打卡
* 适用于云函数部署

## 使用方法（以腾讯云函数为例）
### 准备
* [下载](https://github.com/ChiyukiRuon/Auto_QCZJ/archive/refs/heads/main.zip)本项目的压缩包
* 抓包获取**nid**和**openid**，抓包教程可以参考原项目内的链接

### 本地配置
* 解压下载好的压缩包，进入项目文件夹
* 进入config文件夹，复制`config.yaml.example`并**删除`.example`后缀**，你可以任意修改文件名，脚本会自动读取后缀名为`yaml`的配置文件
* 打开你的yaml配置文件，修改**nid**、**cardNo**、**openid**，其中nid和openid需要自己抓包，cardNo为青年大学习打卡用的昵称
* 返回上一级文件夹，在文件夹内右键，选择**在终端中打开**（Mac用户可以打开**终端**，输入`cd downloads/Auto_QCZJ-main`）
* 在终端内运行`pip install -r requirements.txt -t .`安装依赖

### 云函数配置
* 打开[云函数控制台](https://console.cloud.tencent.com/scf)，点击`新建`，选择`从头开始`
* 基础配置：**函数类型**选择`事件函数`，**运行环境**选择`Python3.7`，其余可以看情况自定义
* 函数代码：选择`本地上传文件夹`，选择刚刚的文件夹上传；`执行方法`写`index.main_handler`
* 日志配置：可以选启用或者不启用，问题不大
* 高级配置：找到**环境配置**，**执行超时时间**填写`30`
* 触发器配置：选择`自定义创建`，**触发周期**选择`自定义触发周期`，**Cron表达式**填写`0 0 22 * * MON *`，表示在每周一的22：00：00执行本函数
> 关于更多Cron表达式的信息，可以参考腾讯云的 [定时触发器说明](https://cloud.tencent.com/document/product/583/9708)
* **同意协议**并点击**完成**即可成功部署

## 最后
阿里云的[函数计算FC](https://fcnext.console.aliyun.com/overview)，和腾讯云函数差不多，在这里就不过多赘述，遇到问题可以去百度（

