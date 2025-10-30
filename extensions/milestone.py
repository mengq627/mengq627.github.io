"""
Milestone Markdown Extension for MkDocs
支持 GitHub 风格的里程碑显示，包含主里程碑和子记录
"""

import re
import yaml
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class MilestonePreprocessor(Preprocessor):
    """处理 milestone 代码块的预处理器"""
    
    MILESTONE_PATTERN = re.compile(
        r'^```milestone\s*\n(.*?)^```\s*$',
        re.MULTILINE | re.DOTALL
    )
    
    def run(self, lines):
        """处理文本中的所有 milestone 块"""
        text = '\n'.join(lines)
        
        def replace_milestone(match):
            yaml_content = match.group(1)
            return self.render_milestone(yaml_content)
        
        text = self.MILESTONE_PATTERN.sub(replace_milestone, text)
        return text.split('\n')
    
    def render_milestone(self, yaml_content):
        """将 YAML 配置渲染为 HTML"""
        try:
            milestones = yaml.safe_load(yaml_content)
            if not isinstance(milestones, list):
                milestones = [milestones]
            
            html = ['<div class="milestone-container">']
            
            for milestone in milestones:
                html.append(self.render_single_milestone(milestone))
            
            html.append('</div>')
            return '\n'.join(html)
            
        except yaml.YAMLError as e:
            return f'<div class="milestone-error">YAML 解析错误: {e}</div>'
    
    def render_single_milestone(self, milestone):
        """渲染单个里程碑"""
        name = milestone.get('name', '未命名里程碑')
        date = milestone.get('date', '')
        detail = milestone.get('detail', '')
        state = milestone.get('state', 'open')  # 默认为 open
        records = milestone.get('records', [])
        
        # 根据状态设置图标和样式类
        if state == 'closed':
            icon_svg = '<svg class="milestone-icon-svg" viewBox="0 0 16 16" width="16" height="16"><path d="M11.28 6.78a.75.75 0 0 0-1.06-1.06L7.25 8.69 5.78 7.22a.75.75 0 0 0-1.06 1.06l2 2a.75.75 0 0 0 1.06 0l3.5-3.5Z"></path><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0Zm-1.5 0a6.5 6.5 0 1 0-13 0 6.5 6.5 0 0 0 13 0Z"></path></svg>'
            state_class = ' milestone-item-closed'
        else:  # open
            icon_svg = '<svg class="milestone-icon-svg" viewBox="0 0 16 16" width="16" height="16"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>'
            state_class = ' milestone-item-open'
        
        html = [f'<div class="milestone-item{state_class}">']
        
        # 里程碑主节点
        html.append('  <div class="milestone-main">')
        html.append('    <div class="milestone-marker">')
        html.append(f'      <div class="milestone-icon milestone-icon-{state}">{icon_svg}</div>')
        html.append('    </div>')
        html.append('    <div class="milestone-content">')
        html.append(f'      <div class="milestone-header">')
        html.append(f'        <span class="milestone-name">{name}</span>')
        if date:
            html.append(f'        <span class="milestone-date">{date}</span>')
        html.append(f'      </div>')
        if detail:
            html.append(f'      <div class="milestone-detail">{detail}</div>')
        html.append('    </div>')
        html.append('  </div>')
        
        # 子记录
        if records:
            html.append('  <div class="milestone-records">')
            for i, record in enumerate(records):
                is_last = (i == len(records) - 1)
                html.append(self.render_record(record, is_last))
            html.append('  </div>')
        
        html.append('</div>')
        return '\n'.join(html)
    
    def render_record(self, record, is_last=False):
        """渲染单个记录"""
        time = record.get('time', '')
        detail = record.get('detail', '')
        
        last_class = ' milestone-record-last' if is_last else ''
        
        html = [f'    <div class="milestone-record{last_class}">']
        html.append('      <div class="milestone-record-marker">')
        html.append('        <div class="milestone-record-dot"></div>')
        html.append('      </div>')
        html.append('      <div class="milestone-record-content">')
        if time:
            html.append(f'        <span class="milestone-record-time">{time}</span>')
        if detail:
            html.append(f'        <span class="milestone-record-detail">{detail}</span>')
        html.append('      </div>')
        html.append('    </div>')
        return '\n'.join(html)


class MilestoneExtension(Extension):
    """Milestone Markdown 扩展"""
    
    def extendMarkdown(self, md):
        """注册预处理器"""
        md.preprocessors.register(
            MilestonePreprocessor(md),
            'milestone',
            175
        )


def makeExtension(**kwargs):
    """创建扩展实例"""
    return MilestoneExtension(**kwargs)

