#!/usr/bin/env python3
"""
Fantasy Guild Manager CLI
A command-line tool for managing guild members, quests, and resources
that generates a web page for party members to view.
"""

import json
import os
import argparse
from datetime import datetime
from typing import Dict, List, Any
import sys

class GuildManager:
    def __init__(self, data_file="guild_data.json"):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self) -> Dict[str, Any]:
        """Load guild data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print(f"Warning: Could not load {self.data_file}. Starting with empty data.")
        
        # Default guild structure
        return {
            "guild_name": "The Unnamed Guild",
            "guild_description": "A brave band of adventurers",
            "members": {},
            "quests": {},
            "resources": {
                "gold": 0,
                "items": {}
            },
            "announcements": [],
            "last_updated": datetime.now().isoformat()
        }
    
    def save_data(self):
        """Save guild data to JSON file"""
        self.data["last_updated"] = datetime.now().isoformat()
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(f"[+] Guild data saved to {self.data_file}")
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_member(self, name: str, character_class: str, level: int = 1, description: str = ""):
        """Add a new guild member"""
        member_id = name.lower().replace(" ", "_")
        self.data["members"][member_id] = {
            "name": name,
            "class": character_class,
            "level": level,
            "description": description,
            "status": "active",
            "joined_date": datetime.now().isoformat()
        }
        self.save_data()
        print(f"[+] Added {name} (Level {level} {character_class}) to the guild!")
    
    def remove_member(self, name: str):
        """Remove a guild member"""
        member_id = name.lower().replace(" ", "_")
        if member_id in self.data["members"]:
            removed_member = self.data["members"].pop(member_id)
            self.save_data()
            print(f"[+] Removed {removed_member['name']} from the guild.")
        else:
            print(f"[-] Member '{name}' not found.")
    
    def list_members(self):
        """List all guild members"""
        if not self.data["members"]:
            print("No guild members found.")
            return
        
        print("\n=== Guild Members ===")
        for member in self.data["members"].values():
            status_icon = "[ACTIVE]" if member["status"] == "active" else "[INACTIVE]"
            print(f"{status_icon} {member['name']} - Level {member['level']} {member['class']}")
            if member.get("description"):
                print(f"   {member['description']}")
    
    def add_quest(self, title: str, description: str, reward: str = "", difficulty: str = "Normal"):
        """Add a new quest"""
        quest_id = title.lower().replace(" ", "_")
        self.data["quests"][quest_id] = {
            "title": title,
            "description": description,
            "reward": reward,
            "difficulty": difficulty,
            "status": "available",
            "created_date": datetime.now().isoformat()
        }
        self.save_data()
        print(f"[+] Added quest: {title}")
    
    def complete_quest(self, title: str):
        """Mark a quest as completed"""
        quest_id = title.lower().replace(" ", "_")
        if quest_id in self.data["quests"]:
            self.data["quests"][quest_id]["status"] = "completed"
            self.data["quests"][quest_id]["completed_date"] = datetime.now().isoformat()
            self.save_data()
            print(f"[+] Quest '{title}' marked as completed!")
        else:
            print(f"[-] Quest '{title}' not found.")
    
    def list_quests(self):
        """List all quests"""
        if not self.data["quests"]:
            print("No quests found.")
            return
        
        print("\n=== Guild Quests ===")
        for quest in self.data["quests"].values():
            status_icon = "[AVAILABLE]" if quest["status"] == "available" else "[COMPLETED]"
            print(f"{status_icon} {quest['title']} ({quest['difficulty']})")
            print(f"   {quest['description']}")
            if quest.get("reward"):
                print(f"   Reward: {quest['reward']}")
    
    def update_resources(self, gold: int = None, item_name: str = None, item_quantity: int = None):
        """Update guild resources"""
        if gold is not None:
            self.data["resources"]["gold"] += gold
            action = "added" if gold > 0 else "spent"
            print(f"[+] {action.title()} {abs(gold)} gold. Current total: {self.data['resources']['gold']}")
        
        if item_name and item_quantity is not None:
            if item_name not in self.data["resources"]["items"]:
                self.data["resources"]["items"][item_name] = 0
            self.data["resources"]["items"][item_name] += item_quantity
            
            if self.data["resources"]["items"][item_name] <= 0:
                del self.data["resources"]["items"][item_name]
                print(f"[+] Removed {item_name} from inventory")
            else:
                print(f"[+] Updated {item_name}: {self.data['resources']['items'][item_name]}")
        
        self.save_data()
    
    def add_announcement(self, message: str):
        """Add a guild announcement"""
        announcement = {
            "message": message,
            "date": datetime.now().isoformat()
        }
        self.data["announcements"].insert(0, announcement)  # Most recent first
        
        # Keep only the last 10 announcements
        self.data["announcements"] = self.data["announcements"][:10]
        self.save_data()
        print(f"[+] Added announcement: {message}")
    
    def set_guild_info(self, name: str = None, description: str = None):
        """Update guild information"""
        if name:
            self.data["guild_name"] = name
            print(f"[+] Guild name set to: {name}")
        if description:
            self.data["guild_description"] = description
            print(f"[+] Guild description updated")
        self.save_data()
    
    def generate_webpage(self, output_file="guild_page.html"):
        """Generate HTML webpage for party members"""
        from web_generator import generate_guild_webpage
        generate_guild_webpage(self.data, output_file)
        print(f"[+] Generated webpage: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Fantasy Guild Manager CLI")
    parser.add_argument("--data", default="guild_data.json", help="Guild data file")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Member commands
    member_parser = subparsers.add_parser("member", help="Manage guild members")
    member_subparsers = member_parser.add_subparsers(dest="member_action")
    
    add_member_parser = member_subparsers.add_parser("add", help="Add a new member")
    add_member_parser.add_argument("name", help="Member name")
    add_member_parser.add_argument("class", help="Character class")
    add_member_parser.add_argument("--level", type=int, default=1, help="Character level")
    add_member_parser.add_argument("--description", default="", help="Member description")
    
    remove_member_parser = member_subparsers.add_parser("remove", help="Remove a member")
    remove_member_parser.add_argument("name", help="Member name")
    
    member_subparsers.add_parser("list", help="List all members")
    
    # Quest commands
    quest_parser = subparsers.add_parser("quest", help="Manage quests")
    quest_subparsers = quest_parser.add_subparsers(dest="quest_action")
    
    add_quest_parser = quest_subparsers.add_parser("add", help="Add a new quest")
    add_quest_parser.add_argument("title", help="Quest title")
    add_quest_parser.add_argument("description", help="Quest description")
    add_quest_parser.add_argument("--reward", default="", help="Quest reward")
    add_quest_parser.add_argument("--difficulty", default="Normal", help="Quest difficulty")
    
    complete_quest_parser = quest_subparsers.add_parser("complete", help="Complete a quest")
    complete_quest_parser.add_argument("title", help="Quest title")
    
    quest_subparsers.add_parser("list", help="List all quests")
    
    # Resource commands
    resource_parser = subparsers.add_parser("resource", help="Manage resources")
    resource_parser.add_argument("--gold", type=int, help="Add/remove gold")
    resource_parser.add_argument("--item", help="Item name")
    resource_parser.add_argument("--quantity", type=int, help="Item quantity")
    
    # Announcement commands
    announce_parser = subparsers.add_parser("announce", help="Add announcement")
    announce_parser.add_argument("message", help="Announcement message")
    
    # Guild info commands
    info_parser = subparsers.add_parser("info", help="Set guild information")
    info_parser.add_argument("--name", help="Guild name")
    info_parser.add_argument("--description", help="Guild description")
    
    # Web generation
    web_parser = subparsers.add_parser("web", help="Generate webpage")
    web_parser.add_argument("--output", default="guild_page.html", help="Output HTML file")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    guild = GuildManager(args.data)
    
    try:
        if args.command == "member":
            if args.member_action == "add":
                guild.add_member(args.name, getattr(args, 'class'), args.level, args.description)
            elif args.member_action == "remove":
                guild.remove_member(args.name)
            elif args.member_action == "list":
                guild.list_members()
        
        elif args.command == "quest":
            if args.quest_action == "add":
                guild.add_quest(args.title, args.description, args.reward, args.difficulty)
            elif args.quest_action == "complete":
                guild.complete_quest(args.title)
            elif args.quest_action == "list":
                guild.list_quests()
        
        elif args.command == "resource":
            guild.update_resources(args.gold, args.item, args.quantity)
        
        elif args.command == "announce":
            guild.add_announcement(args.message)
        
        elif args.command == "info":
            guild.set_guild_info(args.name, args.description)
        
        elif args.command == "web":
            guild.generate_webpage(args.output)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
