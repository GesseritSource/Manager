#!/usr/bin/env python3
"""
Fantasy Guild Manager - Interactive Menu CLI
A simple, menu-driven interface for managing your guild
"""

import os
import sys
from guild_manager import GuildManager

class GuildMenuCLI:
    def __init__(self):
        self.guild = GuildManager()
        self.running = True
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pause(self):
        """Wait for user to press Enter"""
        input("\nPress Enter to continue...")
    
    def show_main_menu(self):
        """Display the main menu"""
        self.clear_screen()
        print("=" * 50)
        print("    FANTASY GUILD MANAGER    ")
        print("=" * 50)
        print(f"Guild: {self.guild.data['guild_name']}")
        print(f"Description: {self.guild.data['guild_description']}")
        print("=" * 50)
        print()
        print("1. Manage Guild Members")
        print("2. Manage Quests")
        print("3. Manage Resources")
        print("4. Guild Announcements")
        print("5. Guild Settings")
        print("6. Generate Web Page")
        print("7. View Guild Status")
        print("8. Exit")
        print()
    
    def get_choice(self, max_option):
        """Get user's menu choice"""
        while True:
            try:
                choice = int(input(f"Choose an option (1-{max_option}): "))
                if 1 <= choice <= max_option:
                    return choice
                else:
                    print(f"Please enter a number between 1 and {max_option}")
            except ValueError:
                print("Please enter a valid number")
    
    def manage_members_menu(self):
        """Member management submenu"""
        while True:
            self.clear_screen()
            print("GUILD MEMBERS MANAGEMENT")
            print("=" * 30)
            print()
            print("1. Add New Member")
            print("2. Remove Member")
            print("3. List All Members")
            print("4. Back to Main Menu")
            print()
            
            choice = self.get_choice(4)
            
            if choice == 1:
                self.add_member()
            elif choice == 2:
                self.remove_member()
            elif choice == 3:
                self.list_members()
            elif choice == 4:
                break
    
    def add_member(self):
        """Add a new guild member"""
        print("\n--- Add New Member ---")
        name = input("Member name: ").strip()
        if not name:
            print("Name cannot be empty!")
            self.pause()
            return
        
        character_class = input("Character class (e.g., Wizard, Fighter, Rogue): ").strip()
        if not character_class:
            character_class = "Adventurer"
        
        try:
            level = int(input("Level (default 1): ") or "1")
        except ValueError:
            level = 1
        
        description = input("Description (optional): ").strip()
        
        self.guild.add_member(name, character_class, level, description)
        self.pause()
    
    def remove_member(self):
        """Remove a guild member"""
        print("\n--- Remove Member ---")
        if not self.guild.data["members"]:
            print("No members to remove!")
            self.pause()
            return
        
        print("\nCurrent members:")
        for i, member in enumerate(self.guild.data["members"].values(), 1):
            print(f"{i}. {member['name']}")
        
        try:
            choice = int(input("\nSelect member to remove (number): "))
            members_list = list(self.guild.data["members"].values())
            if 1 <= choice <= len(members_list):
                member_name = members_list[choice - 1]['name']
                confirm = input(f"Remove {member_name}? (y/N): ").lower()
                if confirm == 'y':
                    self.guild.remove_member(member_name)
                else:
                    print("Cancelled.")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")
        
        self.pause()
    
    def list_members(self):
        """List all guild members"""
        print("\n--- Guild Members ---")
        self.guild.list_members()
        self.pause()
    
    def manage_quests_menu(self):
        """Quest management submenu"""
        while True:
            self.clear_screen()
            print("QUEST MANAGEMENT")
            print("=" * 20)
            print()
            print("1. Add New Quest")
            print("2. Complete Quest")
            print("3. List All Quests")
            print("4. Back to Main Menu")
            print()
            
            choice = self.get_choice(4)
            
            if choice == 1:
                self.add_quest()
            elif choice == 2:
                self.complete_quest()
            elif choice == 3:
                self.list_quests()
            elif choice == 4:
                break
    
    def add_quest(self):
        """Add a new quest"""
        print("\n--- Add New Quest ---")
        title = input("Quest title: ").strip()
        if not title:
            print("Title cannot be empty!")
            self.pause()
            return
        
        description = input("Quest description: ").strip()
        if not description:
            description = "No description provided"
        
        reward = input("Reward (optional): ").strip()
        
        print("\nDifficulty levels:")
        print("1. Easy")
        print("2. Normal")
        print("3. Hard")
        print("4. Legendary")
        
        diff_choice = self.get_choice(4)
        difficulties = ["Easy", "Normal", "Hard", "Legendary"]
        difficulty = difficulties[diff_choice - 1]
        
        self.guild.add_quest(title, description, reward, difficulty)
        self.pause()
    
    def complete_quest(self):
        """Mark a quest as completed"""
        print("\n--- Complete Quest ---")
        available_quests = [q for q in self.guild.data["quests"].values() if q["status"] == "available"]
        
        if not available_quests:
            print("No available quests to complete!")
            self.pause()
            return
        
        print("\nAvailable quests:")
        for i, quest in enumerate(available_quests, 1):
            print(f"{i}. {quest['title']}")
        
        try:
            choice = int(input("\nSelect quest to complete (number): "))
            if 1 <= choice <= len(available_quests):
                quest_title = available_quests[choice - 1]['title']
                self.guild.complete_quest(quest_title)
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")
        
        self.pause()
    
    def list_quests(self):
        """List all quests"""
        print("\n--- Guild Quests ---")
        self.guild.list_quests()
        self.pause()
    
    def manage_resources_menu(self):
        """Resource management submenu"""
        while True:
            self.clear_screen()
            print("RESOURCE MANAGEMENT")
            print("=" * 22)
            print(f"Current Gold: {self.guild.data['resources']['gold']}")
            print()
            print("1. Add/Remove Gold")
            print("2. Add Item to Inventory")
            print("3. Remove Item from Inventory")
            print("4. View All Resources")
            print("5. Back to Main Menu")
            print()
            
            choice = self.get_choice(5)
            
            if choice == 1:
                self.manage_gold()
            elif choice == 2:
                self.add_item()
            elif choice == 3:
                self.remove_item()
            elif choice == 4:
                self.view_resources()
            elif choice == 5:
                break
    
    def manage_gold(self):
        """Add or remove gold"""
        print("\n--- Manage Gold ---")
        print(f"Current gold: {self.guild.data['resources']['gold']}")
        
        try:
            amount = int(input("Enter amount (positive to add, negative to remove): "))
            self.guild.update_resources(gold=amount)
        except ValueError:
            print("Please enter a valid number!")
        
        self.pause()
    
    def add_item(self):
        """Add item to inventory"""
        print("\n--- Add Item ---")
        item_name = input("Item name: ").strip()
        if not item_name:
            print("Item name cannot be empty!")
            self.pause()
            return
        
        try:
            quantity = int(input("Quantity: ") or "1")
            self.guild.update_resources(item_name=item_name, item_quantity=quantity)
        except ValueError:
            print("Please enter a valid number!")
        
        self.pause()
    
    def remove_item(self):
        """Remove item from inventory"""
        print("\n--- Remove Item ---")
        items = self.guild.data['resources']['items']
        
        if not items:
            print("No items in inventory!")
            self.pause()
            return
        
        print("\nCurrent inventory:")
        item_list = list(items.items())
        for i, (item, qty) in enumerate(item_list, 1):
            print(f"{i}. {item} (x{qty})")
        
        try:
            choice = int(input("\nSelect item to remove (number): "))
            if 1 <= choice <= len(item_list):
                item_name = item_list[choice - 1][0]
                current_qty = item_list[choice - 1][1]
                
                remove_qty = int(input(f"Remove how many {item_name}? (max {current_qty}): "))
                if remove_qty > 0:
                    self.guild.update_resources(item_name=item_name, item_quantity=-remove_qty)
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")
        
        self.pause()
    
    def view_resources(self):
        """View all resources"""
        print("\n--- Guild Resources ---")
        print(f"💰 Gold: {self.guild.data['resources']['gold']}")
        
        items = self.guild.data['resources']['items']
        if items:
            print("\nInventory:")
            for item, quantity in items.items():
                print(f"   {item}: {quantity}")
        else:
            print("\nInventory: Empty")
        
        self.pause()
    
    def manage_announcements_menu(self):
        """Announcements management submenu"""
        while True:
            self.clear_screen()
            print("GUILD ANNOUNCEMENTS")
            print("=" * 23)
            print()
            print("1. Add New Announcement")
            print("2. View All Announcements")
            print("3. Back to Main Menu")
            print()
            
            choice = self.get_choice(3)
            
            if choice == 1:
                self.add_announcement()
            elif choice == 2:
                self.view_announcements()
            elif choice == 3:
                break
    
    def add_announcement(self):
        """Add a new announcement"""
        print("\n--- Add Announcement ---")
        message = input("Announcement message: ").strip()
        if not message:
            print("Message cannot be empty!")
            self.pause()
            return
        
        self.guild.add_announcement(message)
        self.pause()
    
    def view_announcements(self):
        """View all announcements"""
        print("\n--- Guild Announcements ---")
        announcements = self.guild.data.get('announcements', [])
        
        if not announcements:
            print("No announcements yet.")
        else:
            for i, announcement in enumerate(announcements, 1):
                print(f"{i}. {announcement['message']}")
                print(f"   Date: {announcement['date']}")
                print()
        
        self.pause()
    
    def guild_settings_menu(self):
        """Guild settings submenu"""
        while True:
            self.clear_screen()
            print("GUILD SETTINGS")
            print("=" * 16)
            print()
            print("1. Change Guild Name")
            print("2. Change Guild Description")
            print("3. Back to Main Menu")
            print()
            
            choice = self.get_choice(3)
            
            if choice == 1:
                self.change_guild_name()
            elif choice == 2:
                self.change_guild_description()
            elif choice == 3:
                break
    
    def change_guild_name(self):
        """Change guild name"""
        print("\n--- Change Guild Name ---")
        print(f"Current name: {self.guild.data['guild_name']}")
        new_name = input("New guild name: ").strip()
        
        if new_name:
            self.guild.set_guild_info(name=new_name)
        else:
            print("Name cannot be empty!")
        
        self.pause()
    
    def change_guild_description(self):
        """Change guild description"""
        print("\n--- Change Guild Description ---")
        print(f"Current description: {self.guild.data['guild_description']}")
        new_description = input("New guild description: ").strip()
        
        if new_description:
            self.guild.set_guild_info(description=new_description)
        else:
            print("Description cannot be empty!")
        
        self.pause()
    
    def generate_webpage(self):
        """Generate the guild webpage"""
        print("\n--- Generate Web Page ---")
        filename = input("Web page filename (default: guild_page.html): ").strip()
        if not filename:
            filename = "guild_page.html"
        
        if not filename.endswith('.html'):
            filename += '.html'
        
        self.guild.generate_webpage(filename)
        print(f"\nWeb page generated: {filename}")
        print("\nTo host this page:")
        print("1. Upload the HTML file to any web hosting service")
        print("2. Or use a local server: python -m http.server 8000")
        print("3. Or share the file directly with your party members")
        
        self.pause()
    
    def view_guild_status(self):
        """View complete guild status"""
        self.clear_screen()
        print("GUILD STATUS OVERVIEW")
        print("=" * 25)
        print(f"Guild: {self.guild.data['guild_name']}")
        print(f"Description: {self.guild.data['guild_description']}")
        print()
        
        # Members summary
        members = self.guild.data['members']
        print(f"Members: {len(members)}")
        if members:
            for member in members.values():
                print(f"   - {member['name']} (Level {member['level']} {member['class']})")
        print()
        
        # Quests summary
        quests = self.guild.data['quests']
        available = sum(1 for q in quests.values() if q['status'] == 'available')
        completed = sum(1 for q in quests.values() if q['status'] == 'completed')
        print(f"Quests: {available} available, {completed} completed")
        print()
        
        # Resources summary
        print(f"💰 Gold: {self.guild.data['resources']['gold']}")
        items = self.guild.data['resources']['items']
        print(f"Items: {len(items)} different types")
        print()
        
        # Recent announcements
        announcements = self.guild.data.get('announcements', [])
        print(f"Recent Announcements: {len(announcements)}")
        
        self.pause()
    
    def run(self):
        """Main program loop"""
        while self.running:
            self.show_main_menu()
            choice = self.get_choice(8)
            
            if choice == 1:
                self.manage_members_menu()
            elif choice == 2:
                self.manage_quests_menu()
            elif choice == 3:
                self.manage_resources_menu()
            elif choice == 4:
                self.manage_announcements_menu()
            elif choice == 5:
                self.guild_settings_menu()
            elif choice == 6:
                self.generate_webpage()
            elif choice == 7:
                self.view_guild_status()
            elif choice == 8:
                print("\nThanks for using Fantasy Guild Manager!")
                self.running = False

def main():
    try:
        cli = GuildMenuCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
