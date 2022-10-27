# import matplotlib.pyplot as plt
#
# plt.bar([0, 1, 2, 3], [5, 6, 7, 8])
# plt.show()

# import matplotlib.pyplot as plt
# import matplotlib
#
# data = [5, 6, 7, 8]
# labels = ['a', 'b', 'c', 'd']
# colors = ['red', 'yellow', 'blue', 'black']
#
# plt.bar(range(len(data)), data, color=colors, width=0.5)
# plt.xticks(range(len(data)), labels)
# for i in range(len(data)):
#     plt.text(x=i-0.02, y=data[i]+0.1, s='%d' % data[i])
# plt.xlabel('x-data')
# plt.ylabel('y-data')
# plt.title('matplotlib.pyplot')
# plt.show()

# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def auto_label(rects):
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height), # put the detail data
#                     xy=(rect.get_x() + rect.get_width() / 2, height), # get the center location.
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
#
#
# def auto_text(rects):
#     for rect in rects:
#         ax.text(rect.get_x(), rect.get_height(), rect.get_height(), ha='left', va='bottom')
#
#
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
#
# index = np.arange(len(labels))
# width = 0.2
#
# fig, ax = plt.subplots()
# rect1 = ax.bar(index - width / 2, men_means, color ='dodgerblue', width=width, label ='Men')
# rect2 = ax.bar(index + width / 2, women_means, color ='coral', width=width, label ='Women')
#
# ax.set_title('Scores by gender')
# ax.set_xticks(ticks=index)
# ax.set_xticklabels(labels)
# ax.set_ylabel('Scores')
#
# ax.set_ylim(0, 50)
# # auto_label(rect1)
# # auto_label(rect2)
# auto_text(rect1)
# auto_text(rect2)
#
# ax.legend(loc='upper right', frameon=False)
# fig.tight_layout()
# # plt.savefig('2.tif', dpi=300)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# courses = ["语文", "数学", "英语", "物理", "化学", "生物"]
# x_arange = np.arange(len(courses))  # [0 1 2 3 4 5]，相当于x轴上的坐标序列
# scores_zhangsan = [76, 98, 67, 95, 90, 82]
# scores_lisi = [96, 72, 98, 69, 72, 81]
#
# bar_width = 0.35  # 一个bar的宽度，注意x轴每两项的刻度的间距为1，注意合理设置宽度
#
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 防止中文乱码
#
# """
# 绘制条形图，各入参的含义：
# x_arange - bar_width / 2：第一个bar在x轴上的中心值，每个刻度值减一半bar宽度得到，第二个bar则是加一半bar宽度；
# scores_zhangsan：bar高度，这里也就是分数值；
# bar_width：bar宽度；
# label：标签
# """
# plt.bar(x_arange - bar_width / 2, scores_zhangsan, bar_width, label="张三")
# plt.bar(x_arange + bar_width / 2, scores_lisi, bar_width, label="李四")
#
# # 在各个bar上标注数值，使用zip()来同步遍历x_arange, scores_zhangsan, scores_lisi
# for x, score_zhangsan, score_lisi in zip(x_arange, scores_zhangsan, scores_lisi):
#     """
#     各入参含义：
#     x - bar_width / 2：所需绘制的数值在x轴的位置；
#     score_zhangsan + 1：所需绘制的数值在y轴的位置，加个1是为了在数值和bar顶部留点空隙；
#     score_zhangsan：所需绘制的数值；
#     ha='center'：对齐方式，这里居中；
#     fontsize=12：字号大小
#     """
# plt.text(x - bar_width / 2, score_zhangsan + 1, score_zhangsan, ha='center', fontsize=12)
# plt.text(x + bar_width / 2, score_lisi + 1, score_lisi, ha='center', fontsize=12)
#
# plt.xlabel("考试科目")
# plt.ylabel("分数")
# plt.xticks(x_arange, labels=courses)  # x轴上的刻度用courses的项来绘制
# plt.title("张三和李四的各科成绩对比")
# plt.legend()
# plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


