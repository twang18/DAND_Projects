# 探索美国单车共享数据
### 项目概述及目的

在本项目中，我将利用 Python 探索与以下三大美国城市的自行车共享系统相关的数据：芝加哥、纽约和华盛顿。我将编写代码导入数据，并通过计算描述性统计数据回答有趣的问题。还将写一个脚本，该脚本会接受原始输入并在终端中创建交互式体验，以展现这些统计信息。

### 数据集详情

- 数据集中提供了三座城市 2017 年上半年的数据。三个数据文件都包含相同的核心6列：

  - 起始时间 Start Time（例如 2017-01-01 00:07:57）
  - 结束时间 End Time（例如 2017-01-01 00:20:53）
  - 骑行时长 Trip Duration（例如 776 秒）
  - 起始车站 Start Station（例如百老汇街和巴里大道）
  - 结束车站 End Station（例如塞奇威克街和北大道）
  - 用户类型 User Type（订阅者 Subscriber/Registered 或客户Customer/Casual）

  芝加哥和纽约市文件还包含以下两列：

  - 性别 Gender
  - 出生年份 Birth Year

## 问题

我将编写代码并回答以下关于自行车共享数据的问题：

- 起始时间（Start Time 列）中哪个月份最常见？
- 起始时间中，一周的哪一天（比如 Monday, Tuesday）最常见？ 
- 起始时间中，一天当中哪个小时最常见？
- 总骑行时长（Trip Duration）是多久，平均骑行时长是多久？
- 哪个起始车站（Start Station）最热门，哪个结束车站（End Station）最热门？
- 哪一趟行程最热门（即，哪一个起始站点与结束站点的组合最热门）？
- 每种用户类型有多少人？
- 每种性别有多少人？
- 出生年份最早的是哪一年、最晚的是哪一年，最常见的是哪一年？

### 软件的安装

要完成此项目，需要安装以下软件：

- Python 3。Python 标准库中的以下软件包可能有用：*csv*、*pprint*、*datetime* 和 *time*。
- 文本编辑器，例如 [Sublime](https://www.sublimetext.com/) 或 [Atom](https://atom.io/)。
- 终端应用（Mac 和 Linux 上的终端和 Windows 上的 Cygwin）。

### 文件描述

- bikeshare.py: python代码文件
- 三个城市的单车数据集：chicago.csv, new_york_city.csv, washington.csv
- README.md

