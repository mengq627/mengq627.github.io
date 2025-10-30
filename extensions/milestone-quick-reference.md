# Milestone 快速参考

## 最简示例

````markdown
```milestone
- name: 我的第一个目标
  date: 2026.12.31
  state: open
  detail: 完成这个重要的目标
  records:
    - time: 2026.01.01
      detail: 开始行动
    - time: 2026.06.01
      detail: 完成一半
```
````

## 状态图标说明

- **`state: open`** - 进行中 🟢
  - 显示绿色圆圈图标（GitHub Issue Open 状态）
  
- **`state: closed`** - 已完成 🟣
  - 显示紫色勾选图标（GitHub Issue Closed 状态）

## 多个里程碑

````markdown
```milestone
- name: 目标 A
  date: 2026.03.01
  state: closed
  detail: 第一个目标（已完成）
  records:
    - time: 2026.01.15
      detail: 开始准备

- name: 目标 B
  date: 2026.06.01
  state: open
  detail: 第二个目标（进行中）
  records:
    - time: 2026.04.01
      detail: 启动项目
    - time: 2026.05.01
      detail: 取得进展
```
````

## 可选字段

所有字段都是可选的（除了 name），可以灵活使用：

````markdown
```milestone
# 只有名称（默认 state 为 open）
- name: 简单目标

# 名称 + 状态
- name: 已完成的目标
  state: closed

# 名称 + 日期
- name: 有截止日期的目标
  date: 2026.12.31
  state: open

# 名称 + 描述
- name: 有详细说明的目标
  detail: 这是一个详细的说明
  state: open

# 完整配置
- name: 完整目标
  date: 2026.12.31
  state: closed
  detail: 详细说明
  records:
    - time: 2026.01.01
      detail: 第一步
```
````

## 日期格式建议

虽然可以使用任何格式，但推荐：

- `2026.10.1`
- `2026-10-01`
- `2026/10/01`
- `10月1日`

## 图标 Emoji 建议

可以在描述中添加 emoji：

```markdown
- name: 🎯 学习目标
  detail: 📚 完成 10 本书的阅读
  records:
    - time: 2026.01
      detail: ✅ 读完第一本
    - time: 2026.02
      detail: 📖 正在读第二本
```

## 注意事项

1. **YAML 缩进**：使用 2 个空格缩进
2. **连字符位置**：列表项的 `-` 前面不要有缩进
3. **冒号后空格**：`name:` 后面要有空格
4. **中文冒号**：使用英文冒号 `:` 而不是中文冒号 `：`

## 错误示例 ❌

```yaml
# 错误：使用了中文冒号
- name： 目标名称

# 错误：冒号后没有空格
- name:目标名称

# 错误：缩进不一致
- name: 目标
    records:
  - time: 时间

# 错误：忘记了列表的 -
  name: 目标
  records:
    time: 时间
```

## 正确示例 ✅

```yaml
- name: 目标名称
  date: 2026.10.1
  state: open
  detail: 目标描述
  records:
    - time: 2026.01.01
      detail: 记录详情
    - time: 2026.02.01
      detail: 另一个记录
```

## 测试你的配置

1. 编辑 `docs/milestone.md`
2. 保存文件
3. 刷新浏览器（如果 `mkdocs serve` 正在运行）
4. 查看效果

如果出现错误，MkDocs 会在终端显示错误信息。


## 使用提示

---

💡 **使用提示**：你可以编辑这个页面，添加自己的里程碑和记录！

## 配置格式说明

使用以下 YAML 格式在 markdown 文件中添加里程碑：

````markdown
```milestone
- name: 里程碑名称
  date: 日期
  state: open  # 或 closed
  detail: 详细描述
  records:
    - time: 记录时间
      detail: 记录详情
    - time: 另一个时间
      detail: 另一个记录
```
````

每个字段说明：
- `name`: 里程碑的名称（必填）
- `date`: 里程碑的目标日期（可选）
- `state`: 里程碑状态（可选，默认为 `open`）
  - `open`: 进行中，显示绿色圆圈图标（GitHub Issue Open）
  - `closed`: 已完成，显示紫色勾选图标（GitHub Issue Closed）
- `detail`: 里程碑的详细描述（可选）
- `records`: 子记录列表（可选）
  - `time`: 记录的时间
  - `detail`: 记录的详细内容