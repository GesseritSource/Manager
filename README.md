# Fantasy Guild Manager CLI

A command-line tool for managing fantasy guild members, quests, and resources that generates beautiful web pages for your party members to view.

## Features

- **Guild Member Management**: Add, remove, and track guild members with classes, levels, and descriptions
- **Quest System**: Create and manage quests with different difficulty levels and rewards
- **Resource Tracking**: Monitor guild gold and inventory items
- **Announcements**: Post guild-wide announcements for your party
- **Web Page Generation**: Create beautiful HTML pages that party members can view
- **Data Persistence**: All data is stored in JSON format for easy backup and portability

## Installation

No external dependencies required! Just Python 3.6+ and the files in this directory.

## Quick Start

1. **Set up your guild information:**
   ```bash
   python guild_manager.py info --name "The Dragon Slayers" --description "Elite adventurers protecting the realm"
   ```

2. **Add some guild members:**
   ```bash
   python guild_manager.py member add "Aria Stormwind" "Wizard" --level 12 --description "Master of elemental magic"
   python guild_manager.py member add "Thorin Ironbeard" "Fighter" --level 10 --description "Veteran warrior and guild protector"
   python guild_manager.py member add "Luna Shadowstep" "Rogue" --level 11 --description "Silent blade and scout extraordinaire"
   ```

3. **Create some quests:**
   ```bash
   python guild_manager.py quest add "The Lost Temple" "Investigate the mysterious temple discovered in the Whispering Woods" --reward "500 gold and ancient artifacts" --difficulty "Hard"
   python guild_manager.py quest add "Goblin Raids" "Clear out the goblin camps threatening local villages" --reward "200 gold per camp" --difficulty "Normal"
   ```

4. **Update guild resources:**
   ```bash
   python guild_manager.py resource --gold 1500
   python guild_manager.py resource --item "Health Potions" --quantity 25
   python guild_manager.py resource --item "Mithril Ore" --quantity 3
   ```

5. **Post an announcement:**
   ```bash
   python guild_manager.py announce "Guild meeting this Friday at 8 PM! We'll be planning our assault on the Lost Temple."
   ```

6. **Generate the web page:**
   ```bash
   python guild_manager.py web --output guild_page.html
   ```

## Command Reference

### Guild Information
```bash
# Set guild name and description
python guild_manager.py info --name "Your Guild Name" --description "Your guild description"
```

### Member Management
```bash
# Add a new member
python guild_manager.py member add "Character Name" "Class" --level 5 --description "Optional description"

# Remove a member
python guild_manager.py member remove "Character Name"

# List all members
python guild_manager.py member list
```

### Quest Management
```bash
# Add a new quest
python guild_manager.py quest add "Quest Title" "Quest description" --reward "Quest reward" --difficulty "Easy|Normal|Hard|Legendary"

# Mark quest as completed
python guild_manager.py quest complete "Quest Title"

# List all quests
python guild_manager.py quest list
```

### Resource Management
```bash
# Add/remove gold
python guild_manager.py resource --gold 500     # Add 500 gold
python guild_manager.py resource --gold -200    # Spend 200 gold

# Add/remove items
python guild_manager.py resource --item "Sword of Power" --quantity 1    # Add item
python guild_manager.py resource --item "Health Potion" --quantity -5    # Use 5 potions
```

### Announcements
```bash
# Add a guild announcement
python guild_manager.py announce "Your announcement message here"
```

### Web Page Generation
```bash
# Generate HTML page (default: guild_page.html)
python guild_manager.py web

# Generate with custom filename
python guild_manager.py web --output my_guild.html
```

## Data Storage

All guild data is stored in `guild_data.json` by default. You can specify a different file with the `--data` flag:

```bash
python guild_manager.py --data my_guild.json member list
```

## Web Page Features

The generated HTML page includes:
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Beautiful Styling**: Modern gradient backgrounds and card layouts
- **Guild Overview**: Name, description, and last updated time
- **Member Profiles**: Character cards with class, level, and descriptions
- **Quest Board**: Available and completed quests with difficulty indicators
- **Resource Tracker**: Guild gold and inventory items
- **Announcements**: Recent guild announcements with timestamps

## Example Workflow

1. **Guild Master** uses the CLI to manage all guild data
2. **Guild Master** runs `python guild_manager.py web` to generate the HTML page
3. **Guild Master** shares the HTML file with party members (via file share, web hosting, etc.)
4. **Party Members** open the HTML file in any web browser to view current guild status

## Tips

- Use descriptive quest titles and member names for better organization
- Regular announcements keep your party engaged
- The web page auto-refreshes data whenever you regenerate it
- Keep backups of your `guild_data.json` file
- You can host the generated HTML on any web server for remote access

## File Structure

```
Guild manager/
├── guild_manager.py    # Main CLI application
├── web_generator.py    # HTML generation module
├── requirements.txt    # Dependencies (none needed!)
├── README.md          # This file
├── guild_data.json    # Your guild data (created automatically)
└── guild_page.html    # Generated web page (created when you run 'web' command)
```

Happy adventuring! 🗡️✨
