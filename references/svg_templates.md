# SVG 图表模板库

## 1. 基础流程图模板

```svg
<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义箭头标记 -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3498db"/>
    </marker>
  </defs>
  
  <!-- 开始节点 -->
  <ellipse cx="100" cy="200" rx="60" ry="30" fill="#27ae60" stroke="#1e8449" stroke-width="2"/>
  <text x="100" y="205" text-anchor="middle" fill="white" font-size="14">开始</text>
  
  <!-- 流程节点1 -->
  <rect x="220" y="170" width="120" height="60" rx="8" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
  <text x="280" y="205" text-anchor="middle" fill="white" font-size="14">步骤1</text>
  
  <!-- 流程节点2 -->
  <rect x="420" y="170" width="120" height="60" rx="8" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
  <text x="480" y="205" text-anchor="middle" fill="white" font-size="14">步骤2</text>
  
  <!-- 结束节点 -->
  <ellipse cx="680" cy="200" rx="60" ry="30" fill="#e74c3c" stroke="#c0392b" stroke-width="2"/>
  <text x="680" y="205" text-anchor="middle" fill="white" font-size="14">结束</text>
  
  <!-- 连接线 -->
  <line x1="160" y1="200" x2="220" y2="200" stroke="#3498db" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="340" y1="200" x2="420" y2="200" stroke="#3498db" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="540" y1="200" x2="620" y2="200" stroke="#3498db" stroke-width="2" marker-end="url(#arrowhead)"/>
</svg>
```

## 2. 层级结构图（树状图）

```svg
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg">
  <!-- 根节点 -->
  <rect x="350" y="20" width="100" height="50" rx="8" fill="#9b59b6" stroke="#8e44ad" stroke-width="2"/>
  <text x="400" y="52" text-anchor="middle" fill="white" font-size="14">根节点</text>
  
  <!-- 一级节点 -->
  <rect x="150" y="150" width="100" height="50" rx="8" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
  <text x="200" y="182" text-anchor="middle" fill="white" font-size="14">分支A</text>
  
  <rect x="350" y="150" width="100" height="50" rx="8" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
  <text x="400" y="182" text-anchor="middle" fill="white" font-size="14">分支B</text>
  
  <rect x="550" y="150" width="100" height="50" rx="8" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
  <text x="600" y="182" text-anchor="middle" fill="white" font-size="14">分支C</text>
  
  <!-- 二级节点 -->
  <rect x="50" y="280" width="80" height="40" rx="6" fill="#2ecc71" stroke="#27ae60" stroke-width="2"/>
  <text x="90" y="305" text-anchor="middle" fill="white" font-size="12">A-1</text>
  
  <rect x="170" y="280" width="80" height="40" rx="6" fill="#2ecc71" stroke="#27ae60" stroke-width="2"/>
  <text x="210" y="305" text-anchor="middle" fill="white" font-size="12">A-2</text>
  
  <!-- 连接线 -->
  <line x1="400" y1="70" x2="200" y2="150" stroke="#bdc3c7" stroke-width="2"/>
  <line x1="400" y1="70" x2="400" y2="150" stroke="#bdc3c7" stroke-width="2"/>
  <line x1="400" y1="70" x2="600" y2="150" stroke="#bdc3c7" stroke-width="2"/>
  
  <line x1="200" y1="200" x2="90" y2="280" stroke="#bdc3c7" stroke-width="2"/>
  <line x1="200" y1="200" x2="210" y2="280" stroke="#bdc3c7" stroke-width="2"/>
</svg>
```

## 3. 循环/迭代图

```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义箭头 -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#e74c3c"/>
    </marker>
  </defs>
  
  <!-- 外圈 -->
  <circle cx="200" cy="200" r="150" fill="none" stroke="#ecf0f1" stroke-width="20"/>
  
  <!-- 进度弧 -->
  <path d="M 200 50 A 150 150 0 1 1 199 50" fill="none" stroke="#3498db" stroke-width="20" stroke-linecap="round"/>
  
  <!-- 中心文字 -->
  <circle cx="200" cy="200" r="80" fill="#2c3e50"/>
  <text x="200" y="190" text-anchor="middle" fill="white" font-size="16">循环过程</text>
  <text x="200" y="215" text-anchor="middle" fill="#bdc3c7" font-size="12">Iteration</text>
  
  <!-- 阶段标记 -->
  <circle cx="200" cy="50" r="25" fill="#e74c3c" stroke="#c0392b" stroke-width="3"/>
  <text x="200" y="56" text-anchor="middle" fill="white" font-size="12">1</text>
  
  <circle cx="350" cy="200" r="25" fill="#f39c12" stroke="#d68910" stroke-width="3"/>
  <text x="350" y="206" text-anchor="middle" fill="white" font-size="12">2</text>
  
  <circle cx="200" cy="350" r="25" fill="#27ae60" stroke="#1e8449" stroke-width="3"/>
  <text x="200" y="356" text-anchor="middle" fill="white" font-size="12">3</text>
  
  <circle cx="50" cy="200" r="25" fill="#9b59b6" stroke="#8e44ad" stroke-width="3"/>
  <text x="50" y="206" text-anchor="middle" fill="white" font-size="12">4</text>
</svg>
```

## 4. 对比矩阵图

```svg
<svg viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
  <!-- 背景 -->
  <rect x="50" y="50" width="500" height="200" fill="#f8f9fa" rx="8"/>
  
  <!-- 表头 -->
  <rect x="50" y="50" width="150" height="50" fill="#2c3e50"/>
  <text x="125" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">特性</text>
  
  <rect x="200" y="50" width="175" height="50" fill="#3498db"/>
  <text x="287" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">方案A</text>
  
  <rect x="375" y="50" width="175" height="50" fill="#e74c3c"/>
  <text x="462" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">方案B</text>
  
  <!-- 行1 -->
  <rect x="50" y="100" width="150" height="50" fill="#ecf0f1"/>
  <text x="125" y="130" text-anchor="middle" font-size="13">性能</text>
  
  <rect x="200" y="100" width="175" height="50" fill="#d5f5e3"/>
  <text x="287" y="130" text-anchor="middle" font-size="13">⭐⭐⭐⭐⭐</text>
  
  <rect x="375" y="100" width="175" height="50" fill="#fadbd8"/>
  <text x="462" y="130" text-anchor="middle" font-size="13">⭐⭐⭐</text>
  
  <!-- 行2 -->
  <rect x="50" y="150" width="150" height="50" fill="#ecf0f1"/>
  <text x="125" y="180" text-anchor="middle" font-size="13">易用性</text>
  
  <rect x="200" y="150" width="175" height="50" fill="#fadbd8"/>
  <text x="287" y="180" text-anchor="middle" font-size="13">⭐⭐⭐</text>
  
  <rect x="375" y="150" width="175" height="50" fill="#d5f5e3"/>
  <text x="462" y="180" text-anchor="middle" font-size="13">⭐⭐⭐⭐⭐</text>
  
  <!-- 行3 -->
  <rect x="50" y="200" width="150" height="50" fill="#ecf0f1"/>
  <text x="125" y="230" text-anchor="middle" font-size="13">成本</text>
  
  <rect x="200" y="200" width="175" height="50" fill="#fadbd8"/>
  <text x="287" y="230" text-anchor="middle" font-size="13">高</text>
  
  <rect x="375" y="200" width="175" height="50" fill="#d5f5e3"/>
  <text x="462" y="230" text-anchor="middle" font-size="13">低</text>
</svg>
```

## 5. 概念关系图（概念图）

```svg
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg">
  <!-- 中心概念 -->
  <circle cx="400" cy="250" r="70" fill="#9b59b6" stroke="#8e44ad" stroke-width="3"/>
  <text x="400" y="245" text-anchor="middle" fill="white" font-size="16" font-weight="bold">核心概念</text>
  <text x="400" y="265" text-anchor="middle" fill="#e8daef" font-size="12">Central Idea</text>
  
  <!-- 关联概念1 -->
  <ellipse cx="150" cy="150" rx="80" ry="45" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
  <text x="150" y="145" text-anchor="middle" fill="white" font-size="14">相关概念A</text>
  <text x="150" y="162" text-anchor="middle" fill="#d6eaf8" font-size="11">属性说明</text>
  
  <!-- 关联概念2 -->
  <ellipse cx="650" cy="150" rx="80" ry="45" fill="#e74c3c" stroke="#c0392b" stroke-width="2"/>
  <text x="650" y="145" text-anchor="middle" fill="white" font-size="14">相关概念B</text>
  <text x="650" y="162" text-anchor="middle" fill="#fadbd8" font-size="11">属性说明</text>
  
  <!-- 关联概念3 -->
  <ellipse cx="150" cy="350" rx="80" ry="45" fill="#27ae60" stroke="#1e8449" stroke-width="2"/>
  <text x="150" y="345" text-anchor="middle" fill="white" font-size="14">相关概念C</text>
  <text x="150" y="362" text-anchor="middle" fill="#d5f5e3" font-size="11">属性说明</text>
  
  <!-- 关联概念4 -->
  <ellipse cx="650" cy="350" rx="80" ry="45" fill="#f39c12" stroke="#d68910" stroke-width="2"/>
  <text x="650" y="345" text-anchor="middle" fill="white" font-size="14">相关概念D</text>
  <text x="650" y="362" text-anchor="middle" fill="#fdebd0" font-size="11">属性说明</text>
  
  <!-- 连接线 -->
  <line x1="230" y1="150" x2="330" y2="220" stroke="#bdc3c7" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="570" y1="150" x2="470" y2="220" stroke="#bdc3c7" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="230" y1="350" x2="330" y2="280" stroke="#bdc3c7" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="570" y1="350" x2="470" y2="280" stroke="#bdc3c7" stroke-width="2" stroke-dasharray="5,5"/>
  
  <!-- 关系标注 -->
  <text x="280" y="180" text-anchor="middle" fill="#7f8c8d" font-size="11">包含</text>
  <text x="520" y="180" text-anchor="middle" fill="#7f8c8d" font-size="11">依赖</text>
  <text x="280" y="320" text-anchor="middle" fill="#7f8c8d" font-size="11">扩展</text>
  <text x="520" y="320" text-anchor="middle" fill="#7f8c8d" font-size="11">实现</text>
</svg>
```

## 6. 时间线图

```svg
<svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg">
  <!-- 主时间线 -->
  <line x1="100" y1="150" x2="700" y2="150" stroke="#bdc3c7" stroke-width="4"/>
  
  <!-- 时间点1 -->
  <circle cx="150" cy="150" r="12" fill="#3498db" stroke="#2980b9" stroke-width="3"/>
  <text x="150" y="115" text-anchor="middle" font-size="13" font-weight="bold">阶段1</text>
  <text x="150" y="195" text-anchor="middle" font-size="11" fill="#7f8c8d">描述文字</text>
  
  <!-- 时间点2 -->
  <circle cx="300" cy="150" r="12" fill="#27ae60" stroke="#1e8449" stroke-width="3"/>
  <text x="300" y="115" text-anchor="middle" font-size="13" font-weight="bold">阶段2</text>
  <text x="300" y="195" text-anchor="middle" font-size="11" fill="#7f8c8d">描述文字</text>
  
  <!-- 时间点3 -->
  <circle cx="450" cy="150" r="12" fill="#f39c12" stroke="#d68910" stroke-width="3"/>
  <text x="450" y="115" text-anchor="middle" font-size="13" font-weight="bold">阶段3</text>
  <text x="450" y="195" text-anchor="middle" font-size="11" fill="#7f8c8d">描述文字</text>
  
  <!-- 时间点4 -->
  <circle cx="600" cy="150" r="12" fill="#e74c3c" stroke="#c0392b" stroke-width="3"/>
  <text x="600" y="115" text-anchor="middle" font-size="13" font-weight="bold">阶段4</text>
  <text x="600" y="195" text-anchor="middle" font-size="11" fill="#7f8c8d">描述文字</text>
  
  <!-- 箭头 -->
  <polygon points="700,145 700,155 715,150" fill="#bdc3c7"/>
</svg>
```

## 7. 韦恩图（集合关系）

```svg
<svg viewBox="0 0 500 350" xmlns="http://www.w3.org/2000/svg">
  <!-- 集合A -->
  <circle cx="180" cy="175" r="100" fill="#3498db" fill-opacity="0.3" stroke="#3498db" stroke-width="2"/>
  <text x="120" y="120" font-size="16" font-weight="bold" fill="#2980b9">集合A</text>
  
  <!-- 集合B -->
  <circle cx="320" cy="175" r="100" fill="#e74c3c" fill-opacity="0.3" stroke="#e74c3c" stroke-width="2"/>
  <text x="360" y="120" font-size="16" font-weight="bold" fill="#c0392b">集合B</text>
  
  <!-- 交集 -->
  <text x="250" y="170" text-anchor="middle" font-size="13" fill="#7f8c8d">交集</text>
  <text x="250" y="190" text-anchor="middle" font-size="11" fill="#7f8c8d">A∩B</text>
  
  <!-- 独有A -->
  <text x="130" y="180" text-anchor="middle" font-size="12" fill="#2980b9">仅A</text>
  
  <!-- 独有B -->
  <text x="370" y="180" text-anchor="middle" font-size="12" fill="#c0392b">仅B</text>
  
  <!-- 图例 -->
  <rect x="50" y="290" width="400" height="40" fill="#f8f9fa" rx="5"/>
  <text x="70" y="315" font-size="12" fill="#7f8c8d">说明：两个集合的交集表示同时属于A和B的元素</text>
</svg>
```

## 8. 思维导图风格（放射状）

```svg
<svg viewBox="0 0 600 500" xmlns="http://www.w3.org/2000/svg">
  <!-- 中心节点 -->
  <ellipse cx="300" cy="250" rx="90" ry="50" fill="#9b59b6" stroke="#8e44ad" stroke-width="3"/>
  <text x="300" y="245" text-anchor="middle" fill="white" font-size="16" font-weight="bold">中心主题</text>
  <text x="300" y="265" text-anchor="middle" fill="#e8daef" font-size="12">核心概念</text>
  
  <!-- 分支1 -->
  <line x1="390" y1="250" x2="480" y2="150" stroke="#3498db" stroke-width="3"/>
  <ellipse cx="520" cy="130" rx="70" ry="35" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
  <text x="520" y="125" text-anchor="middle" fill="white" font-size="13">分支主题1</text>
  <text x="520" y="142" text-anchor="middle" fill="#d6eaf8" font-size="10">说明文字</text>
  
  <!-- 分支2 -->
  <line x1="390" y1="250" x2="480" y2="350" stroke="#e74c3c" stroke-width="3"/>
  <ellipse cx="520" cy="370" rx="70" ry="35" fill="#e74c3c" stroke="#c0392b" stroke-width="2"/>
  <text x="520" y="365" text-anchor="middle" fill="white" font-size="13">分支主题2</text>
  <text x="520" y="382" text-anchor="middle" fill="#fadbd8" font-size="10">说明文字</text>
  
  <!-- 分支3 -->
  <line x1="210" y1="250" x2="120" y2="150" stroke="#27ae60" stroke-width="3"/>
  <ellipse cx="80" cy="130" rx="70" ry="35" fill="#27ae60" stroke="#1e8449" stroke-width="2"/>
  <text x="80" y="125" text-anchor="middle" fill="white" font-size="13">分支主题3</text>
  <text x="80" y="142" text-anchor="middle" fill="#d5f5e3" font-size="10">说明文字</text>
  
  <!-- 分支4 -->
  <line x1="210" y1="250" x2="120" y2="350" stroke="#f39c12" stroke-width="3"/>
  <ellipse cx="80" cy="370" rx="70" ry="35" fill="#f39c12" stroke="#d68910" stroke-width="2"/>
  <text x="80" y="365" text-anchor="middle" fill="white" font-size="13">分支主题4</text>
  <text x="80" y="382" text-anchor="middle" fill="#fdebd0" font-size="10">说明文字</text>
</svg>
```

## 使用建议

1. **根据内容选择图表类型**
   - 流程类 → 流程图
   - 层级类 → 树状图
   - 关系类 → 关系图/韦恩图
   - 时间类 → 时间线
   - 对比类 → 对比矩阵

2. **配色方案**
   - 主色：#2c3e50（深蓝灰）
   - 强调色：#3498db（亮蓝）
   - 成功/正向：#27ae60（绿）
   - 警告/注意：#f39c12（橙）
   - 错误/负向：#e74c3c（红）
   - 辅助色：#9b59b6（紫）

3. **SVG优化**
   - 使用viewBox确保响应式
   - 内联样式，不依赖外部CSS
   - 添加aria-label提升可访问性
   - 控制文件大小，避免过度复杂
