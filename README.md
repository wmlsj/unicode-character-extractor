# unicode-character-extractor Unicode字符提取工具
这是一个简单的 Python 脚本,可以从字符串中提取所有的Unicode字符,并打印出它们的16进制编码到一个可以直接使用的C语言数组。

## 运行样例
```
get_unicodes("一二三四五六七八九十人大中小天年月日时分季山川水火木金土王国家行来去了还就说道事上下左右前后进出问与给在地也和或但被主至第会其子同较着性今以及为什么怎么样真的没有不可以如果因为所以要不然但是可是那谢谢不客气请问劳驾调试设置连接网络运行等待时间结束高低电平上拉下拉内部外部时钟源频率测量传感采集转换光敏电阻红外循迹转动运动控制显示彩屏触摸按键蜂鸣器喇叭继电器核心板开发板仿真器下载器编译器延时函数子程序中断事件状态机振荡器采样定时脉冲宽度调制直流转交流反馈系统闭环开环压力温度测量")
```
输出结果：
```
static final int[] specificUnicodes = {
0x4e00, 0x4e8c, 0x4e09, 0x56db, 0x4e94, 0x516d, 0x4e03, 0x516b, 0x4e5d, 0x5341, 0x4eba, 0x5927, 0x4e2d, 0x5c0f, 0x5929, 0x5e74, 
0x6708, 0x65e5, 0x65f6, 0x5206, 0x5b63, 0x5c71, 0x5ddd, 0x6c34, 0x706b, 0x6728, 0x91d1, 0x571f, 0x738b, 0x56fd, 0x5bb6, 0x884c, 
0x6765, 0x53bb, 0x4e86, 0x8fd8, 0x5c31, 0x8bf4, 0x9053, 0x4e8b, 0x4e0a, 0x4e0b, 0x5de6, 0x53f3, 0x524d, 0x540e, 0x8fdb, 0x51fa, 
0x95ee, 0x4e0e, 0x7ed9, 0x5728, 0x5730, 0x4e5f, 0x548c, 0x6216, 0x4f46, 0x88ab, 0x4e3b, 0x81f3, 0x7b2c, 0x4f1a, 0x5176, 0x5b50, 
0x540c, 0x8f83, 0x7740, 0x6027, 0x4eca, 0x4ee5, 0x53ca, 0x4e3a, 0x4ec0, 0x4e48, 0x600e, 0x6837, 0x771f, 0x7684, 0x6ca1, 0x6709, 
0x4e0d, 0x53ef, 0x5982, 0x679c, 0x56e0, 0x6240, 0x8981, 0x7136, 0x662f, 0x90a3, 0x8c22, 0x5ba2, 0x6c14, 0x8bf7, 0x52b3, 0x9a7e, 
0x8c03, 0x8bd5, 0x8bbe, 0x7f6e, 0x8fde, 0x63a5, 0x7f51, 0x7edc, 0x8fd0, 0x7b49, 0x5f85, 0x95f4, 0x7ed3, 0x675f, 0x9ad8, 0x4f4e, 
0x7535, 0x5e73, 0x62c9, 0x5185, 0x90e8, 0x5916, 0x949f, 0x6e90, 0x9891, 0x7387, 0x6d4b, 0x91cf, 0x4f20, 0x611f, 0x91c7, 0x96c6, 
0x8f6c, 0x6362, 0x5149, 0x654f, 0x963b, 0x7ea2, 0x5faa, 0x8ff9, 0x52a8, 0x63a7, 0x5236, 0x663e, 0x793a, 0x5f69, 0x5c4f, 0x89e6, 
0x6478, 0x6309, 0x952e, 0x8702, 0x9e23, 0x5668, 0x5587, 0x53ed, 0x7ee7, 0x6838, 0x5fc3, 0x677f, 0x5f00, 0x53d1, 0x4eff, 0x8f7d, 
0x7f16, 0x8bd1, 0x5ef6, 0x51fd, 0x6570, 0x7a0b, 0x5e8f, 0x65ad, 0x4ef6, 0x72b6, 0x6001, 0x673a, 0x632f, 0x8361, 0x5b9a, 0x50, 
0x57, 0x4d, 0x8109, 0x51b2, 0x5bbd, 0x5ea6, 0x76f4, 0x6d41, 0x4ea4, 0x53cd, 0x9988, 0x7cfb, 0x7edf, 0x95ed, 0x73af, 0x538b, 
0x529b, 0x6e29, };
```
