### matplotlib如何使用，绘制折线图，matplotlib如何设置线条颜色和风格

  ```python
  from matplotlib import pyplot as plt
  #设置图形大小
  plt.figure(figsize=(20,8),dpi=80)
  plt.plot(x,y,color="cyan",linestyle="",linewidth="",alpha=0.4,label="")
  #设置网格
  plt.grid(alpha="",linestyle="")
  #设置图例
  plt.legend(loc="",prop=my_font)

  #设置图信息
  plt.xlabel("时间",fontproperties=my_font)
  plt.ylabel("时间",fontproperties=my_font)
  plt.title("",fontproperties=my_font)

  #保存
  plt.savefig("./baidu.png")
  plt.show()
  ````

### matplotlib如何设置x轴的刻度
  ```python
  #设置显示中文
  from matplotlib import font_manager
  my_font = font_manager.FontProperties(fname="")
  plt.xticks(x,["","",""],fontproperties=my_font,rotation=45)
  ```

### 常见统计图的对比
  - 折线图：展示数据的变化情况
  - 散点图：两个属性上的数据的相关情况，展示离群点
  - 直方图：统计连续的数据
  - 条形图：统计离散的数据





##简历

##### 项目描述


##### 个人职责


##### 技术描述
-------------------
- requests模块发送请求，获取响应
- 如何处理反扒
  - 购买代理ip，实现代理ip池，使用***定期检测ip的可用性，维护代理ip池的质量，怎么取
  - cookie池，cookie怎么来的，多久更新一次，cookie怎么取，怎么用，登录如何实现
  - 验证码如何处理
  - 手机号等如何处理
  - 账号如何处理
  - js生成的数据，生成的参数，页面的跳转如何处理
- 去重
  - url去重如何实现
  - 数据去重怎么做的
- 存储
  - 用什么存，使用什么模块在python中操作数据库，新的数据更新还是直接插入
  - redis集群

- 实现持久化的爬虫
- 断点续爬的爬虫
- 实现分布式的爬虫

- 数据的处理和清洗，提供数据给前端，进行展示
  - pandas，numpy

-----------------------
- scrapy模块发送请求，获取响应
- 如何处理反扒
  - 购买代理ip，实现代理ip池，使用***定期检测ip的可用性，维护代理ip池的质量，怎么取
  - cookie池，cookie怎么来的，多久更新一次，cookie怎么取，怎么用，登录如何实现
  - 验证码如何处理
  - 手机号等如何处理
  - 账号如何处理
  - js生成的数据，生成的参数，页面的跳转如何处理
- 去重
  - url去重如何实现
  - 数据去重怎么做的
- 存储
  - 用什么存，使用什么模块在python中操作数据库，新的数据更新还是直接插入
  - redis集群

- 实现持久化的爬虫
- 断点续爬的爬虫
- 实现分布式的爬虫

- 数据的处理和清洗，提供数据给前端，进行展示
  - pandas，numpy

  -----------------------
  - scrapy_redis模块发送请求，获取响应
  - 如何处理反扒
    - 购买代理ip，实现代理ip池，使用***定期检测ip的可用性，维护代理ip池的质量，怎么取
    - cookie池，cookie怎么来的，多久更新一次，cookie怎么取，怎么用，登录如何实现
    - 验证码如何处理
    - 手机号等如何处理
    - 账号如何处理
    - js生成的数据，生成的参数，页面的跳转如何处理
  - 去重
    - url去重如何实现
    - 数据去重怎么做的
  - 存储
    - 存到mysql，如何建表，为什么这样建表
    - 用什么存，使用什么模块在python中操作数据库，新的数据更新还是直接插入
    - redis集群

  - 实现持久化的爬虫
  - 断点续爬的爬虫
  - 实现分布式的爬虫

  - 数据的处理和清洗，提供数据给前端，进行展示
    - pandas，numpy


##### 项目环境
  - pycharm+python+linux+scrapy+requests+mysql+redis+mongodb
