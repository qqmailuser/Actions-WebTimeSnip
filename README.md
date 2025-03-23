# WebTimeSnip


## 简介

WebTimeSnip 是一个利用 GitHub Actions 的自动网页截图的工具。
它通过 GitHub Actions 每6小时访问一次指定网页并截图, 然后将截图保存到仓库中, 方便你查看和回顾网页的历史快照。

## 如何使用

1.  fork 仓库到你的 GitHub 账户。
2.  启用 GitHub Actions：
    * 在你的 GitHub 仓库中, 点击 "Actions" 选项卡。
    * 如果需要, 点击 "I understand my workflows, go ahead and enable them" 按钮。
3.  设置仓库读写权限：
    * 在你的 GitHub 仓库中, 点击 "Settings" 选项卡。
    * 在左侧边栏中, 点击 "Actions" -> "General"。
    * 在 "Workflow permissions" 部分, 确保选中 "Read and write permissions"。

## 截图

![截图](bilibili/demo.png)

## 许可证

MIT

