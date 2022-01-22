from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/8f38c2a68e7a4c2e3f6c9.jpg"
  

          
rizoel = "✧ 𝑷𝑹𝑶𝑭𝑬𝑺𝑺𝑶𝑹 𝑺𝑷𝑨𝑴𝑺𝑻𝑬𝑹𝑺 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **ᴘʀᴏғᴇssᴏʀ sᴘᴀᴍsᴛᴇʀs**  : `{rizoelversion}`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/AGORABOT_INFO"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/AGORA_SPAM_OFFICIAL")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Agora-OS/PROFESSOR-SPAMSTERS")
        ]
        ]
        )
    
