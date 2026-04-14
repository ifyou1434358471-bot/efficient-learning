#!/usr/bin/env python3
"""
高效学习助手 - 学习笔记生成脚本
用于将学习内容填充到HTML模板中，生成精美的学习笔记
"""

import re
from datetime import datetime
from pathlib import Path

class LearningNoteGenerator:
    """学习笔记生成器"""
    
    def __init__(self, template_path=None):
        """初始化生成器"""
        if template_path is None:
            # 默认模板路径
            script_dir = Path(__file__).parent
            template_path = script_dir.parent / "templates" / "learning_template.html"
        
        self.template_path = Path(template_path)
        self.template = self._load_template()
    
    def _load_template(self):
        """加载HTML模板"""
        with open(self.template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def generate(self, content_data, output_path=None):
        """
        生成学习笔记HTML文件
        
        Args:
            content_data: 字典，包含学习内容
            output_path: 输出文件路径
        
        Returns:
            生成的HTML字符串
        """
        html = self.template
        
        # 基础信息替换
        html = html.replace('{{TITLE}}', content_data.get('title', '学习笔记'))
        html = html.replace('{{SUBTITLE}}', content_data.get('subtitle', ''))
        html = html.replace('{{DIFFICULTY}}', content_data.get('difficulty', '⭐⭐'))
        html = html.replace('{{ESTIMATED_TIME}}', content_data.get('estimated_time', '20分钟'))
        html = html.replace('{{GENERATED_DATE}}', datetime.now().strftime('%Y-%m-%d'))
        
        # 内容模块替换
        html = html.replace('{{EXAMPLES_CONTENT}}', content_data.get('examples', ''))
        html = html.replace('{{CONCEPT_CONTENT}}', content_data.get('concept', ''))
        html = html.replace('{{MEMORY_CONTENT}}', content_data.get('memory', ''))
        html = html.replace('{{DIAGRAMS_CONTENT}}', content_data.get('diagrams', ''))
        
        # 扩展导航和内容
        additional_nav = content_data.get('additional_nav', '')
        html = html.replace('{{ADDITIONAL_NAV}}', additional_nav)
        
        extension_modules = content_data.get('extensions', '')
        html = html.replace('{{EXTENSION_MODULES}}', extension_modules)
        
        # 保存文件
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"学习笔记已生成: {output_path}")
        
        return html


def create_example_card(title, content, emoji="📌", card_type=""):
    """创建例子卡片HTML"""
    type_class = f" {card_type}" if card_type else ""
    return f'''
    <div class="card{type_class}">
        <div class="card-title">{emoji} {title}</div>
        <div class="card-content">{content}</div>
    </div>
    '''


def create_concept_box(definition, title="核心定义"):
    """创建概念定义框HTML"""
    return f'''
    <div class="concept-box">
        <h3>{title}</h3>
        <p class="definition">{definition}</p>
    </div>
    '''


def create_key_points(points):
    """创建要点列表HTML"""
    items = ''.join([f'<li>{point}</li>' for point in points])
    return f'<ul class="key-points">{items}</ul>'


def create_memory_card(mnemonic, explanation=""):
    """创建记忆法卡片HTML"""
    explanation_html = f'<p class="explanation">{explanation}</p>' if explanation else ''
    return f'''
    <div class="memory-card">
        <div class="card-title">🎯 记忆口诀</div>
        <div class="mnemonic">{mnemonic}</div>
        {explanation_html}
    </div>
    '''


def create_diagram_container(svg_content, caption=""):
    """创建图示容器HTML"""
    caption_html = f'<div class="diagram-caption">{caption}</div>' if caption else ''
    return f'''
    <div class="diagram-container">
        {svg_content}
        {caption_html}
    </div>
    '''


def create_exercise(question, answer, level="basic"):
    """创建练习题HTML"""
    level_names = {
        "basic": "基础题",
        "intermediate": "进阶题", 
        "advanced": "挑战题"
    }
    level_text = level_names.get(level, "练习题")
    
    return f'''
    <div class="exercise">
        <div class="exercise-header">
            <strong>{question}</strong>
            <span class="exercise-level level-{level}">{level_text}</span>
        </div>
        <button class="toggle-answer" onclick="this.nextElementSibling.classList.toggle('show')">查看答案</button>
        <div class="answer">
            <strong>答案：</strong>{answer}
        </div>
    </div>
    '''


def create_tip(content):
    """创建提示框HTML"""
    return f'<div class="tip">{content}</div>'


def create_caution(content):
    """创建警告框HTML"""
    return f'<div class="caution">{content}</div>'


# 使用示例
if __name__ == "__main__":
    # 示例数据
    content = {
        "title": "递归",
        "subtitle": "Recursion - 编程中最优雅的思维方式",
        "difficulty": "⭐⭐⭐",
        "estimated_time": "30分钟",
        "examples": "<p>示例内容...</p>",
        "concept": "<p>概念讲解...</p>",
        "memory": "<p>记忆方法...</p>",
        "diagrams": "<p>图示内容...</p>"
    }
    
    # 生成笔记
    generator = LearningNoteGenerator()
    generator.generate(content, "递归_学习笔记.html")
