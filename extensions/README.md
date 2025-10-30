# Milestone 里程碑扩展

这是一个自定义的 MkDocs Markdown 扩展，用于展示类似 GitHub 风格的里程碑页面。

## 功能特性

- ✨ 支持多个里程碑展示
- 📝 每个里程碑可以包含多个子记录
- 🎨 美观的 Material 主题适配样式
- 🌓 支持深色/浅色主题自动切换
- 📱 响应式设计，适配移动端

## 安装配置

### 1. 确保项目结构

```
your-project/
├── docs/
│   ├── milestone.md          # 里程碑页面
│   └── stylesheets/
│       └── milestone.css     # 样式文件
├── extensions/
│   ├── __init__.py
│   └── milestone.py          # 扩展代码
├── mkdocs.yml               # 配置文件
└── requirements.txt         # 依赖包
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

确保 `requirements.txt` 包含：
```
mkdocs
mkdocs-material
PyYAML
```

### 3. 配置 mkdocs.yml

添加以下配置：

```yaml
# 添加 Markdown 扩展
markdown_extensions:
  # ... 其他扩展
  - extensions.milestone       # 自定义里程碑扩展

# 添加 CSS 样式
extra_css:
  - stylesheets/milestone.css

# 添加导航
nav:
  - 里程碑: milestone.md
```

## 使用方法

在你的 Markdown 文件中使用以下格式：

````markdown
# 我的里程碑

```milestone
- name: 里程碑一：2026.10.1
  date: 2026.10.1
  state: closed
  detail: 完成 xxx 项目的核心功能开发
  records:
    - time: 2026.10.2
      detail: 更近一步了，完成了数据库设计
    - time: 2026.10.5
      detail: 坚持训练了，实现了用户认证模块

- name: 里程碑二：学习新技能
  date: 2026.11.1
  state: open
  detail: 掌握某项新技能
  records:
    - time: 2026.10.15
      detail: 开始学习基础知识
    - time: 2026.10.20
      detail: 完成第一个实践项目
```
````

## 配置字段说明

### 里程碑字段

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `name` | string | 是 | 里程碑名称 |
| `date` | string | 否 | 里程碑目标日期 |
| `state` | string | 否 | 里程碑状态：`open`（进行中，绿色）或 `closed`（已完成，紫色），默认为 `open` |
| `detail` | string | 否 | 里程碑详细描述 |
| `records` | array | 否 | 子记录列表 |

### 记录字段

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `time` | string | 否 | 记录时间 |
| `detail` | string | 否 | 记录详细内容 |

## 样式定制

如果你想自定义样式，可以编辑 `docs/stylesheets/milestone.css` 文件。

主要 CSS 类：

- `.milestone-container` - 整个里程碑容器
- `.milestone-item` - 单个里程碑项
- `.milestone-main` - 里程碑主节点
- `.milestone-icon` - 里程碑图标 (默认 📍)
- `.milestone-content` - 里程碑内容区域
- `.milestone-name` - 里程碑名称
- `.milestone-date` - 里程碑日期
- `.milestone-detail` - 里程碑详细描述
- `.milestone-records` - 记录列表容器
- `.milestone-record` - 单个记录
- `.milestone-record-dot` - 记录节点圆点
- `.milestone-record-time` - 记录时间
- `.milestone-record-detail` - 记录详情

## 开发和测试

### 本地预览

```bash
mkdocs serve
```

然后访问 http://127.0.0.1:8000/milestone/

### 构建站点

```bash
mkdocs build
```

## 示例效果

里程碑会渲染成类似 GitHub Issue 的时间线样式：

- **状态图标**：
  - `state: open` - 绿色圆圈图标（GitHub Issue Open）
  - `state: closed` - 紫色勾选图标（GitHub Issue Closed）
- 主里程碑显示为大的卡片，带有状态图标
- 子记录显示在左侧有连线的时间线上
- 记录以较小的字体显示，节点为圆点
- 支持悬停效果和动画

## 技术实现

- **语言**: Python
- **框架**: MkDocs + Material Theme
- **依赖**: markdown, PyYAML
- **类型**: Markdown Preprocessor Extension

## 许可

MIT License

## 作者

Created for mengq627.github.io project

