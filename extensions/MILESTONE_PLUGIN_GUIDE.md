# Milestone 插件使用指南

## 概述

这是一个为 MkDocs + Material 主题定制的里程碑展示插件，灵感来自 GitHub Milestone 的设计。

## 已完成的工作

### 1. 创建的文件

- `extensions/milestone.py` - 核心扩展代码
- `extensions/__init__.py` - Python 包初始化文件
- `docs/stylesheets/milestone.css` - 样式文件
- `docs/milestone.md` - 示例里程碑页面
- `extensions/README.md` - 详细使用文档

### 2. 修改的文件

- `requirements.txt` - 添加了 PyYAML 依赖
- `mkdocs.yml` - 添加了扩展配置、CSS 引用和导航项

## 快速开始

### 查看效果

MkDocs 开发服务器已经在后台运行，访问：

```
http://127.0.0.1:8000/milestone/
```

### 使用示例

在任何 Markdown 文件中使用以下格式：

````markdown
```milestone
- name: 里程碑标题
  date: 2026.10.1
  status: todo
  detail: 里程碑描述
  records:
    - time: 2026.10.2
      detail: 第一个进展
    - time: 2026.10.5
      detail: 第二个进展
```
````

## 配置格式详解

### YAML 结构

```yaml
- name: 里程碑一：2026.10.1    # 里程碑对象直接作为列表元素
  date: 2026.10.1              # 可选：显示在右上角的日期标签
  status: todo                 # 可选：todo（进行中）或 done（已完成），默认为 todo
  detail: 完成xxx              # 可选：里程碑的详细描述
  records:                     # 可选：里程碑下的记录列表
    - time: 2026.10.2          # 记录时间（以更小字体显示）
      detail: 更近一步了        # 记录详情
    - time: 2026.10.5
      detail: 坚持训练了
```

### 特点

1. **主里程碑**
   - **状态图标**（类似 GitHub Issue）：
     - `status: todo` - 绿色圆圈图标 🟢（进行中）
     - `status: done` - 紫色勾选图标 🟣（已完成）
   - 白色卡片背景
   - 名称加粗显示
   - 日期显示在右上角的标签中

2. **子记录（records）**
   - 显示在左侧有连线的时间线上
   - 圆点节点标记
   - 字体比主里程碑小
   - 悬停时圆点会放大并变色

3. **响应式设计**
   - 桌面端：完整展示
   - 移动端：自适应缩小

4. **主题支持**
   - 浅色主题：白色背景
   - 深色主题：深色背景
   - 自动跟随 Material 主题切换

## 样式定制

### 修改状态颜色

编辑 `docs/stylesheets/milestone.css`：

```css
/* Todo 状态 - 绿色（GitHub Issue Open） */
.milestone-icon-todo {
  background: #1a7f37;  /* 修改这个颜色 */
  color: #ffffff;
}

/* Done 状态 - 紫色（GitHub Issue Closed） */
.milestone-icon-done {
  background: #8250df;  /* 修改这个颜色 */
  color: #ffffff;
}
```

### 修改记录节点颜色

编辑 `docs/stylesheets/milestone.css`：

```css
/* 记录节点颜色 */
.milestone-record-dot {
  border: 2px solid var(--md-accent-fg-color, #667eea);
}
```

### 调整字体大小

```css
/* 里程碑标题 */
.milestone-name {
  font-size: 1.25rem;  /* 调整这个值 */
}

/* 记录详情 */
.milestone-record-detail {
  font-size: 0.875rem;  /* 调整这个值 */
}
```

## 部署到 GitHub Pages

### 方法 1: 手动部署

```bash
# 构建站点
mkdocs build

# 部署到 gh-pages 分支
mkdocs gh-deploy
```

### 方法 2: GitHub Actions 自动部署

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy MkDocs

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
          
      - name: Install dependencies
        run: pip install -r requirements.txt
        
      - name: Build and deploy
        run: mkdocs gh-deploy --force
```

## 常见问题

### Q: 页面显示不正常？

A: 确保：
1. PyYAML 已安装：`pip install PyYAML`
2. CSS 文件路径正确
3. YAML 格式正确（注意缩进）

### Q: 如何添加更多里程碑？

A: 编辑 `docs/milestone.md`，在 milestone 代码块中添加更多项目（以 `-` 开头）

### Q: 可以在多个页面使用吗？

A: 可以！在任何 `.md` 文件中使用 milestone 代码块即可

### Q: 如何修改状态图标的颜色？

A: 编辑 `docs/stylesheets/milestone.css` 中的 `.milestone-icon-todo` 和 `.milestone-icon-done` 类，修改 `background` 属性

## 技术细节

- **类型**: Python Markdown Preprocessor
- **优先级**: 175（在 markdown 处理前执行）
- **工作原理**: 
  1. 扫描 markdown 文件中的 milestone 代码块
  2. 解析 YAML 配置
  3. 生成 HTML 结构
  4. CSS 负责样式渲染

## 进一步定制

如果你想添加更多功能，可以修改 `extensions/milestone.py`：

1. **添加新字段**：在 `render_single_milestone` 或 `render_record` 方法中添加
2. **修改 HTML 结构**：调整 `html.append()` 的内容
3. **添加交互功能**：在 CSS 中添加更多动画，或创建 JS 文件

## 联系方式

如有问题或建议，欢迎在项目中提 issue 或直接修改代码。

---

**享受你的里程碑页面！** 🎉

