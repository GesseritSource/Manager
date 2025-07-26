"""
Web page generator for the Fantasy Guild Manager
Creates beautiful HTML pages that party members can view
"""

from datetime import datetime
from typing import Dict, Any

def generate_guild_webpage(guild_data: Dict[str, Any], output_file: str):
    """Generate a beautiful HTML webpage from guild data"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{guild_data['guild_name']} - Guild Portal</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #333;
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
            position: relative;
        }}
        
        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="2" fill="rgba(255,255,255,0.1)"/></svg>') repeat;
            opacity: 0.3;
        }}
        
        .header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 1;
        }}
        
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
            background: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
            border-left: 5px solid #667eea;
        }}
        
        .section h2 {{
            color: #667eea;
            font-size: 2em;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .member-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }}
        
        .member-card {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease;
        }}
        
        .member-card:hover {{
            transform: translateY(-5px);
        }}
        
        .member-name {{
            font-size: 1.3em;
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
        }}
        
        .member-class {{
            color: #667eea;
            font-weight: 600;
            margin-bottom: 10px;
        }}
        
        .member-description {{
            color: #666;
            font-style: italic;
        }}
        
        .quest-item {{
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            border-left: 4px solid #28a745;
        }}
        
        .quest-item.completed {{
            border-left-color: #6c757d;
            opacity: 0.7;
        }}
        
        .quest-title {{
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
            margin-bottom: 8px;
        }}
        
        .quest-difficulty {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .difficulty-easy {{ background: #d4edda; color: #155724; }}
        .difficulty-normal {{ background: #fff3cd; color: #856404; }}
        .difficulty-hard {{ background: #f8d7da; color: #721c24; }}
        .difficulty-legendary {{ background: #d1ecf1; color: #0c5460; }}
        
        .quest-description {{
            color: #666;
            margin-bottom: 10px;
        }}
        
        .quest-reward {{
            color: #28a745;
            font-weight: 600;
        }}
        
        .resources {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}
        
        .resource-card {{
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }}
        
        .resource-value {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        
        .resource-label {{
            color: #666;
            margin-top: 5px;
        }}
        
        .announcement {{
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 15px;
        }}
        
        .announcement-date {{
            color: #666;
            font-size: 0.9em;
            margin-bottom: 5px;
        }}
        
        .announcement-message {{
            color: #333;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e9ecef;
        }}
        
        .status-active {{
            color: #28a745;
        }}
        
        .status-inactive {{
            color: #dc3545;
        }}
        
        .empty-state {{
            text-align: center;
            color: #666;
            font-style: italic;
            padding: 40px;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2em;
            }}
            
            .content {{
                padding: 20px;
            }}
            
            .section {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>⚔️ {guild_data['guild_name']}</h1>
            <p>{guild_data['guild_description']}</p>
        </div>
        
        <div class="content">
            {generate_announcements_section(guild_data.get('announcements', []))}
            {generate_members_section(guild_data.get('members', {}))}
            {generate_quests_section(guild_data.get('quests', {}))}
            {generate_resources_section(guild_data.get('resources', {}))}
        </div>
        
        <div class="footer">
            <p>Last updated: {format_datetime(guild_data.get('last_updated', ''))}</p>
            <p>Generated by Fantasy Guild Manager CLI</p>
        </div>
    </div>
</body>
</html>"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_announcements_section(announcements):
    """Generate the announcements section"""
    if not announcements:
        return """
        <div class="section">
            <h2>📢 Guild Announcements</h2>
            <div class="empty-state">No announcements at this time.</div>
        </div>"""
    
    announcements_html = ""
    for announcement in announcements:
        date_str = format_datetime(announcement.get('date', ''))
        announcements_html += f"""
        <div class="announcement">
            <div class="announcement-date">{date_str}</div>
            <div class="announcement-message">{announcement['message']}</div>
        </div>"""
    
    return f"""
    <div class="section">
        <h2>📢 Guild Announcements</h2>
        {announcements_html}
    </div>"""

def generate_members_section(members):
    """Generate the guild members section"""
    if not members:
        return """
        <div class="section">
            <h2>👥 Guild Members</h2>
            <div class="empty-state">No guild members yet. The adventure awaits!</div>
        </div>"""
    
    members_html = ""
    for member in members.values():
        status_class = "status-active" if member.get('status') == 'active' else "status-inactive"
        status_icon = "🟢" if member.get('status') == 'active' else "🔴"
        
        description = f'<div class="member-description">{member.get("description", "")}</div>' if member.get("description") else ""
        
        members_html += f"""
        <div class="member-card">
            <div class="member-name">{status_icon} {member['name']}</div>
            <div class="member-class">Level {member.get('level', 1)} {member.get('class', 'Adventurer')}</div>
            {description}
        </div>"""
    
    return f"""
    <div class="section">
        <h2>👥 Guild Members</h2>
        <div class="member-grid">
            {members_html}
        </div>
    </div>"""

def generate_quests_section(quests):
    """Generate the quests section"""
    if not quests:
        return """
        <div class="section">
            <h2>📋 Guild Quests</h2>
            <div class="empty-state">No quests available. Check back later for new adventures!</div>
        </div>"""
    
    # Separate available and completed quests
    available_quests = []
    completed_quests = []
    
    for quest in quests.values():
        if quest.get('status') == 'completed':
            completed_quests.append(quest)
        else:
            available_quests.append(quest)
    
    quests_html = ""
    
    # Available quests first
    for quest in available_quests:
        difficulty_class = f"difficulty-{quest.get('difficulty', 'normal').lower()}"
        reward_html = f'<div class="quest-reward">💰 Reward: {quest["reward"]}</div>' if quest.get("reward") else ""
        
        quests_html += f"""
        <div class="quest-item">
            <div class="quest-title">📋 {quest['title']}</div>
            <span class="quest-difficulty {difficulty_class}">{quest.get('difficulty', 'Normal')}</span>
            <div class="quest-description">{quest['description']}</div>
            {reward_html}
        </div>"""
    
    # Completed quests
    for quest in completed_quests:
        difficulty_class = f"difficulty-{quest.get('difficulty', 'normal').lower()}"
        reward_html = f'<div class="quest-reward">💰 Reward: {quest["reward"]}</div>' if quest.get("reward") else ""
        
        quests_html += f"""
        <div class="quest-item completed">
            <div class="quest-title">✅ {quest['title']} (Completed)</div>
            <span class="quest-difficulty {difficulty_class}">{quest.get('difficulty', 'Normal')}</span>
            <div class="quest-description">{quest['description']}</div>
            {reward_html}
        </div>"""
    
    return f"""
    <div class="section">
        <h2>📋 Guild Quests</h2>
        {quests_html}
    </div>"""

def generate_resources_section(resources):
    """Generate the resources section"""
    resources_html = f"""
    <div class="resource-card">
        <div class="resource-value">💰 {resources.get('gold', 0)}</div>
        <div class="resource-label">Gold</div>
    </div>"""
    
    items = resources.get('items', {})
    if items:
        for item_name, quantity in items.items():
            resources_html += f"""
            <div class="resource-card">
                <div class="resource-value">📦 {quantity}</div>
                <div class="resource-label">{item_name}</div>
            </div>"""
    
    return f"""
    <div class="section">
        <h2>💎 Guild Resources</h2>
        <div class="resources">
            {resources_html}
        </div>
    </div>"""

def format_datetime(iso_string):
    """Format ISO datetime string for display"""
    if not iso_string:
        return "Unknown"
    
    try:
        dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except:
        return iso_string
