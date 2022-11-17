# Auto_QCZJ
适用于云函数部署的青年大学习自动打卡，**仅限浙江地区使用**  
原项目地址[WuliAPO/Fuck_QCZJ](https://github.com/WuliAPO/Fuck_QCZJ)

## 功能
* 可用于多用户打卡
* 适用于云函数部署

## 使用方法（以腾讯云为例）
* ### Windows
1. [下载](https://github.com/ChiyukiRuon/Auto_QCZJ/archive/refs/heads/main.zip)压缩包，解压后进入项目文件夹
2. 进入config文件夹，复制`config.yaml.example`并**删除`.example`后缀**，你可以任意修改文件名，脚本会自动读取后缀名为`yaml`的配置文件
3. 打开你的yaml配置文件，修改**nid**、**cardNo**、**openid**，其中nid和openid需要自己抓包
4. 返回上一级文件夹，在文件夹内右键，选择`在终端中打开`
5. 在终端内运行`pip install -r requirements.txt -t .`
6. 打开[腾讯云函数控制台](https://console.cloud.tencent.com/scf)，点击`新建`，选择`从头开始`
7. **函数名称**可以自定义，**其余保持默认**
8. **函数代码**选择`本地上传文件夹`，选择刚刚的文件夹上传
9. 在**高级配置**内的**环境配置**，`执行超时时间`填写30
10. **触发器配置**选择`自定义创建`-**触发周期**选择`自定义触发周期`-**Cron表达式**填写`0 0 22 * * MON *`，表示在每周一的22：00：00执行本函数
11. **同意协议**并点击**完成**即可成功部署
> 关于更多Cron表达式的信息，可以参考腾讯云的 [定时触发器说明](https://cloud.tencent.com/document/product/583/9708)  

> 抓包教程可以参考原项目内的链接

