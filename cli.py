from manager import InstaProfile, Database
import os
import sys


obj = InstaProfile()
obj.setTARGET("ac3.desu")
obj.login(username=Database.USERNAME, password=Database.PASSWORD)


accinfo = obj.getProfileInfo()

CLEAR = 'clear' if os.name == 'posix' else 'cls'


def show_logo():
    print(r"""
    ____           __        _____ __        ____            
   /  _/___  _____/ /_____ _/ ___// /_____ _/ / /_____  _____
   / // __ \/ ___/ __/ __ `/\__ \/ __/ __ `/ / //_/ _ \/ ___/
 _/ // / / (__  ) /_/ /_/ /___/ / /_/ /_/ / / ,< /  __/ /    
/___/_/ /_/____/\__/\__,_//____/\__/\__,_/_/_/|_|\___/_/     
                        
                           v1.0
                    Made by ZeaCeR#5641                                     
    """)


def show_logo_profile():
    print(r"""
            ____             _____ __   
           / __ \_________  / __(_) /__ 
          / /_/ / ___/ __ \/ /_/ / / _ \
         / ____/ /  / /_/ / __/ / /  __/
        /_/   /_/   \____/_/ /_/_/\___/ 

    """)


def show_help_main_menu():
    print(r"""
Available commands in the home menu,
    [1] help        --> display this text

    [2] target      --> set target if not set
    [3] login       --> login to instagram account

    [4] profile     --> profile menu
    [5] posts       --> posts menu
    [6] followers   --> followers menu 
    [7] followees   --> followees menu
    [8] DUMP ALL    --> Save all data (BETA)
    
    [99] clear      --> Clear Screen/Console
    [100] exit      --> exit the script 
    """)


def show_help_profile_menu():
    print(r"""
Available commands in the home menu,
    [1] help                     --> display this text

    [2] all                      --> Show all information
    [3] username                 --> Username
    [4] profile_id               --> Profile ID
    [5] is_private               --> Is Privatee
    [6] followed_by_viewer       --> Followed by viewer
    [7] mediacount               --> Media Count
    [8] igtv_count               --> IGTV Count
    [9] followers                --> Followers
    [1] followees                --> Followees
    [11] external_url            --> External URL
    [12] is_business_account     --> Is Business Account
    [13] business_category_name  --> Business Category Name
    [14] biography               --> Biography
    [15] blocked_by_viewer       --> Blocked by viewer
    [16] follows_viewer          --> Follows viewer
    [17] full_name               --> Full Name
    [18] has_blocked_viewer      --> Has blocked viewer
    [19] has_highlight_reels     --> Has highlight reels
    [20] has_public_story        --> Has public story
    [21] has_viewable_story      --> Has viewable story
    [22] has_requested_viewer    --> Has requested viewer
    [23] is_verified             --> Is Verified
    [24] requested_by_viewer     --> Requested by viewer
    [25] profile_pic_url         --> Profile pic url

    [26] save                    --> Save all profile info

    [99] clear                   --> Clear Screen
    [100] back                   --> Go back to main menu
    [101] exit                   --> exit app
    """)


def clear_screen():
    os.system(CLEAR)


def ENTIRE_PROGRAM():
    show_logo()

    # Main Menu Option
    mmo = input("home> ").strip()

    if (mmo == 'help') or (mmo == '1'):
        show_help_main_menu()
        input("Press `Enter` to go back!")
        ENTIRE_PROGRAM()

    elif (mmo == 'target') or (mmo == '2'):
        target_username = input("target's username> ").strip()
        target = insta.setTARGET(target=target_username)
        if target:
            print("[+] Target username has been set!")
        else:
            print("[-] Skipping! Target username has been set already!")
        ENTIRE_PROGRAM()

    elif (mmo == 'login') or (mmo == '3'):
        login_username = input("username> ")
        login_password = input("password> ")
        print("[*] Please wait user is logging in!")
        login_status = insta.login(
            username=login_username,
            password=login_password
        )
        if login_status:
            print("[+] Logged in successfully!")
        else:
            print("[+] Skipping! User is already logged in!")
        ENTIRE_PROGRAM()

    elif (mmo == 'profile') or (mmo == '4'):
        show_logo_profile()

        print('[*] Please wait while information is being gathered!')
        profile_info = insta.getProfileInfo()
        print('[+] Done!')

        mm1 = input('profile> ').strip()
        if (mm1 == 'help') or (mm1 == '1'):
            show_help_profile_menu()
            input("Press `Enter` to go back!")
            ENTIRE_PROGRAM()

        elif (mm1 == 'all') or (mm1 == '2'):
            print(f"""
Username: {profile_info['username']}
Profile ID: {profile_info['profile_id']}
Is Private: {profile_info['is_private']}
Followed by viewer: {profile_info['followed_by_viewer']}
Media Count: {profile_info['mediacount']}
IGTV Count: {profile_info['igtv_count']}
Followers: {profile_info['followers']}
Followees: {profile_info['followees']}
External URL: {profile_info['external_url']}
Is Business Account: {profile_info['is_business_account']}
Business Category Name: {profile_info['business_category_name']}
Bography: {profile_info['biography']}
Blocked by viewer: {profile_info['blocked_by_viewer']}
Follows viewer: {profile_info['follows_viewer']}
Full Name: {profile_info['full_name']}
Has blocked viewer: {profile_info['has_blocked_viewer']}
Has highlight reels: {profile_info['has_highlight_reels']}
Has public story: {profile_info['has_public_story']}
Has viewable story: {profile_info['has_viewable_story']}
Has requested viewer: {profile_info['has_requested_viewer']}
Is Verified: {profile_info['is_verified']}
Requested by viewer: {profile_info['requested_by_viewer']}
Profile pic url: {profile_info['profile_pic_url']}
                """)

        elif (mm1 == 'save') or (mm1 == '26'):
            custom_format = input("format [txt / json(default)]>")
            custom_filename = input(
                "custom filename (defaults to username)> ").strip()

            if isinstance(custom_format, str):
                if (custom_format == "txt") or (custom_format == "json"):
                    pass
            else:
                custom_format = False

            if isinstance(custom_filename, str):
                if len(custom_filename) >= 2:
                    pass
                else:
                    custom_filename = None

            if custom_format is False:
                insta.saveProfileInfo(filename=custom_filename)
            else:
                insta.saveProfileInfo(
                    file_format=custom_format,
                    filename=custom_filename
                )

        elif (mm1 == 'clear') or (mm1 == '99'):
            clear_screen()

        elif (mm1 == 'back') or (mm1 == '100'):
            ENTIRE_PROGRAM()

        elif (mm1 == 'exit') or (mm1 == '101'):
            sys.exit("[!!] Have a nice day!")

        else:
            if len(mm1) <= 2:
                items = {
                    '3': 'username',
                    '4': 'profile_id',
                    '5': 'is_private',
                    '6': 'followed_by_viewer',
                    '7': 'mediacount',
                    '8': 'igtv_count',
                    '9': 'followers',
                    '1': 'followees',
                    '12': 'external_url',
                    '13': 'is_business_account',
                    '14': 'business_category_name',
                    '15': 'biography',
                    '16': 'blocked_by_viewer',
                    '17': 'follows_viewer',
                    '18': 'full_name',
                    '19': 'has_blocked_viewer',
                    '20': 'has_highlight_reels',
                    '21': 'has_public_story',
                    '22': 'has_viewable_story',
                    '23': 'has_requested_viewer',
                    '24': 'is_verified',
                    '25': 'requested_by_viewer',
                    '26': 'profile_pic_ur'
                }
                print(profile_info[items[mm1]])

            else:
                try:
                    print(profile_info[mm1])
                except KeyError:
                    print(f"[-] Error: No key named `{mm1}` in data set!")

        ENTIRE_PROGRAM()


if __name__ == "__main__":
    print('[*] Please wait while the object is being instantiated!')
    insta = InstaProfile()
    print('[+] Done!')
    clear_screen()
    ENTIRE_PROGRAM()
