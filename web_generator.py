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
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }}
        
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: #4a5568;
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .section {{
            margin-bottom: 30px;
            background: #f9f9f9;
            border-radius: 5px;
            padding: 20px;
            border-left: 4px solid #4a5568;
        }}
        
        .section h2 {{
            color: #2d3748;
            font-size: 1.5em;
            margin-bottom: 15px;
            font-weight: bold;
        }}
        
        .member-list {{
            list-style: none;
        }}
        
        .member-item {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
        }}
        
        .member-name {{
            font-size: 1.2em;
            font-weight: bold;
            color: #2d3748;
            margin-bottom: 5px;
        }}
        
        .member-class {{
            color: #4a5568;
            font-weight: 500;
            margin-bottom: 8px;
        }}
        
        .member-description {{
            color: #718096;
            font-size: 0.9em;
        }}
        
        .quest-item {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
        }}
        
        .quest-item.completed {{
            background: #f7fafc;
            opacity: 0.8;
        }}
        
        .quest-title {{
            font-size: 1.1em;
            font-weight: bold;
            color: #2d3748;
            margin-bottom: 5px;
        }}
        
        .quest-difficulty {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 3px;
            font-size: 0.8em;
            font-weight: 500;
            margin-bottom: 8px;
        }}
        
        .difficulty-easy {{ background: #c6f6d5; color: #22543d; }}
        .difficulty-normal {{ background: #fef5e7; color: #744210; }}
        .difficulty-hard {{ background: #fed7d7; color: #742a2a; }}
        .difficulty-legendary {{ background: #bee3f8; color: #2a4365; }}
        
        .quest-description {{
            color: #4a5568;
            margin-bottom: 8px;
            font-size: 0.9em;
        }}
        
        .quest-reward {{
            color: #38a169;
            font-weight: 500;
            font-size: 0.9em;
        }}
        
        .resource-list {{
            list-style: none;
        }}
        
        .resource-item {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .resource-name {{
            font-weight: 500;
            color: #2d3748;
        }}
        
        .resource-value {{
            font-weight: bold;
            color: #38a169;
        }}
        
        .announcement {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
        }}
        
        .announcement-date {{
            color: #718096;
            font-size: 0.8em;
            margin-bottom: 5px;
        }}
        
        .announcement-message {{
            color: #2d3748;
        }}
        
        .footer {{
            background: #f7fafc;
            padding: 20px;
            text-align: center;
            color: #718096;
            border-top: 1px solid #e2e8f0;
            font-size: 0.9em;
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
            <h2>Guild Announcements</h2>
            <p>No announcements at this time.</p>
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
        <h2>Guild Announcements</h2>
        {announcements_html}
    </div>"""

def generate_members_section(members):
    """Generate the guild members section"""
    if not members:
        return """
        <div class="section">
            <h2>Guild Members</h2>
            <p>No guild members yet. The adventure awaits!</p>
        </div>"""
    
    members_html = ""
    for member in members.values():
        status = "Active" if member.get('status') == 'active' else "Inactive"
        
        description = f'<div class="member-description">{member.get("description", "")}</div>' if member.get("description") else ""
        
        members_html += f"""
        <div class="member-item">
            <div class="member-name">{member['name']} ({status})</div>
            <div class="member-class">Level {member.get('level', 1)} {member.get('class', 'Adventurer')}</div>
            {description}
        </div>"""
    
    return f"""
    <div class="section">
        <h2>Guild Members</h2>
        <div class="member-list">
            {members_html}
        </div>
    </div>"""

def generate_quests_section(quests):
    """Generate the quests section"""
    if not quests:
        return """
        <div class="section">
            <h2>Guild Quests</h2>
            <p>No quests available. Check back later for new adventures!</p>
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
        reward_html = f'<div class="quest-reward">Reward: {quest["reward"]}</div>' if quest.get("reward") else ""
        
        quests_html += f"""
        <div class="quest-item">
            <div class="quest-title">{quest['title']}</div>
            <span class="quest-difficulty {difficulty_class}">{quest.get('difficulty', 'Normal')}</span>
            <div class="quest-description">{quest['description']}</div>
            {reward_html}
        </div>"""
    
    # Completed quests
    for quest in completed_quests:
        difficulty_class = f"difficulty-{quest.get('difficulty', 'normal').lower()}"
        reward_html = f'<div class="quest-reward">Reward: {quest["reward"]}</div>' if quest.get("reward") else ""
        
        quests_html += f"""
        <div class="quest-item completed">
            <div class="quest-title">{quest['title']} (Completed)</div>
            <span class="quest-difficulty {difficulty_class}">{quest.get('difficulty', 'Normal')}</span>
            <div class="quest-description">{quest['description']}</div>
            {reward_html}
        </div>"""
    
    return f"""
    <div class="section">
        <h2>Guild Quests</h2>
        {quests_html}
    </div>"""

def generate_resources_section(resources):
    """Generate the resources section"""
    resources_html = f"""
    <div class="resource-item">
        <div class="resource-name">Gold</div>
        <div class="resource-value">{resources.get('gold', 0)}</div>
    </div>"""
    
    items = resources.get('items', {})
    if items:
        for item_name, quantity in items.items():
            resources_html += f"""
            <div class="resource-item">
                <div class="resource-name">{item_name}</div>
                <div class="resource-value">{quantity}</div>
            </div>"""
    
    return f"""
    <div class="section">
        <h2>Guild Resources</h2>
        <div class="resource-list">
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
