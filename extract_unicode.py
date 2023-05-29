def get_unicodes(s):
    unicodes = []
    for c in s:
        if c not in unicodes:
            unicodes.append(c)
    # comment = '//' + ''.join(unicodes)
    print('static final int[] specificUnicodes = {')
    # print(comment)
    count = 0
    for unicode in unicodes:
        print(hex(ord(unicode)) + ',', end=' ')
        count += 1
        if count % 16 == 0:
            print()
    print('};')


if __name__ == '__main__':
    get_unicodes(
        "一二三四五六七八九十人大中小天年月日时分季山川水火木金土王国家行来去了还就说道事上下左右前后进出问与给在地也和或但被主至第会其子同较着性今以及为什么怎么样真的没有不可以如果因为所以要不然但是可是那谢谢不客气请问劳驾调试设置连接网络运行等待时间结束高低电平上拉下拉内部外部时钟源频率测量传感采集转换光敏电阻红外循迹转动运动控制显示彩屏触摸按键蜂鸣器喇叭继电器核心板开发板仿真器下载器编译器延时函数子程序中断事件状态机振荡器采样定时PWM脉冲宽度调制直流转交流反馈系统闭环开环压力温度测量"
    )
