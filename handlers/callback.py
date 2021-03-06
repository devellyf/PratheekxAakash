# (C) 2021 All Rights Reserved PratheekProjects

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π πππππ πππππ {message.from_user.mention}</b> β ππππΎπππ ππ ππ π½πππ

ππππ ππ πΌ π½ππ πΏπππππππΏ ππ πππΌπ πππππΎ ππ ππππ ππππππ!

ππππ ππ πΌ πππ½πππΎ ππππππΎπ ππ [πππΌπππππ](https://t.me/pratheek06) & [πΌπΌππΌππ](https://t.me/akshhhxx)....ππΌπΏπ ππππ β€οΈ.

ππππ πΌππ ππππ πΎππΏπ ππ πππ ππππ π½ππ """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π Sα΄α΄α΄α΄Ι΄ Mα΄β π", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "Hα΄α΄‘ Tα΄ Usα΄ Mα΄β β", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "π Cα΄α΄α΄α΄Ι΄α΄s", callback_data="cbcmds")
                ],[
                    InlineKeyboardButton(
                        "ββUα΄α΄α΄α΄α΄s CΚα΄Ι΄Ι΄α΄Κ π£", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "Sα΄α΄α΄α΄Κα΄ CΚα΄α΄ π₯", url=f"https://t.me/{GROUP_SUPPORT}")
                ],[
                ],[
                    InlineKeyboardButton(
                        "π₯ Oα΄‘Ι΄α΄Κ 1", url=f"https://t.me/pratheek06"
                    ),
                    InlineKeyboardButton(
                        "β¨ Oα΄‘Ι΄α΄Κ 2", url=f"https://t.me/akshhhxx")
                ],[
                    InlineKeyboardButton(
                        "π€ π΄πππ ππππ πΆππ π©ππ π€", url="https://github.com/PratheekXD/PratheekxAakash"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

Β» **Press The Button Below To Read The Explanation And See The List Of Available Commands!**

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Basic Cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("Advanced Cmd", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("Owner Cmd", callback_data="cbowner")],
                [InlineKeyboardButton("π Go Back", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **Here Is The Basic Commands**

π§ [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

π§ [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π΄ **Here Is The Advanced Commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **Here Is The Admin Commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π΄ **Here Is The Sudo Commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **Here Is The Owner Commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

π Note: All Commands Owned By This Bot Can Be Executed By The Owner Of The Bot Without Any Exceptions.

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β **HOW TO USE THIS BOT:** β

1.) **First, Add Me To Your Group.**
2.) **Then Promote Me As Admin And Give All Permissions Except Anonymous Admin.**
3.) **Add @{ASSISTANT_NAME} To Your Group Or Type /join to invite.**
4.) **Turn On The Voice Chat First Before Start To Play Music.**

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("π Command List", callback_data="cbhelp")],
                [InlineKeyboardButton("β Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "** Here Is The Control Menu Of Bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("βΈ Pause", callback_data="cbpause"),
                    InlineKeyboardButton("βΆοΈ Resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("β© Skip", callback_data="cbskip"),
                    InlineKeyboardButton("βΉ Stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("β Anti Cmds", callback_data="cbdelcmds")],
                [InlineKeyboardButton("π Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π **This Is The Feature Information:**
        
**β Feature:** !Delete Every Commands Sent By Users To Avoid Spam In Groups!

β Usage:**

 1οΈβ£ To Turn On Feature:
     Β» type `/delcmd on`
    
 2οΈβ£ To Turn Off Feature:
     Β» type `/delcmd off`
      
π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

Β» **Press The Button Below To Read The Explanation And See The List Of Available Commands !**

π¦ __Powered By {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Basic Cmd", callback_data="cblocal"),
                    InlineKeyboardButton("Advanced Cmd", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cblamp"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cblab"),
                ],
                [InlineKeyboardButton("Owner Cmd", callback_data="cbmoon")],
                [InlineKeyboardButton("π Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β **HOW TO USE THIS BOT:** β

1.) **First, Add Me To Your Group.**
2.) **Then Promote Me As Admin And Give All Permissions Except Anonymous Admin.**
3.) **Add @{ASSISTANT_NAME} To Your Group Or Type /join To Invite Her.**
4.) **Turn On The Voice Chat First Before Start To Play Music.**

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π΄ **Here Is The Basic Commands**

π§ [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

π§ [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **Here Is The Advanced Commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π΄ **Here Is The Admin Commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **Here Is The Sudo Commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π΄ **Here Is The Owner Commands**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

π Note: All Commands Owned By This Bot Can Be Executed By The Owner Of The Bot Without Any Exceptions.

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )
