import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("/start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**⊱⋅━═━═[『 𝗠𝗥_𝗫 』](https://t.me/MRv7x)═━═━⋅⊰**\n
● **انا بوت تشغيل القرآن الكريم وتنزيل الفديو**\n
● **اضفني مشرف في مجموعتك لأعمل**\n
● **اتبع مايلي لمعرفه كيفيه الاستخدام**\n
● **اضغط علي ذر طريقه الاستخدام**\n
● **مميزات الروبوت يعمل بجودة فائقه**\n
**⊱⋅━═━═[『 𝗠𝗥_𝗫 』](https://t.me/MR_X_N)═━═━⋅⊰**\n""",
    reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ],
            [
            InlineKeyboardButton( "𝘀𝗼𝗨𝗥𝗰𝗲 𝙈𝙍_𝙓",url=f"https://t.me/MUSTAR_X8"),
            ],
            [
            InlineKeyboardButton("𝗗𝗲𝘃𝗲𝗟𝗼𝗣𝗲𝗥𝘀", url=f"https://t.me/AzkarMusIim"),
              ],
              [ 
                  InlineKeyboardButton(
                         " 🎧¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
            [
                InlineKeyboardButton(" 🤖¦ لتنصيب بوتك ميوزك ", url=f"https://t.me/MR_X_N"),
            ]
         ]
     )
  )

@Client.on_message(
    command(["مبرمج السورس","المستر"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/08d12aa31c5c41e51f6f2.jpg",
        caption=f""" 𝘞𝘌𝘓𝘊𝘖𝘔𝘌 𝘔𝘙_𝘟 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓂄𓆩 𝙼𝚁_𝚇 𓆪𓂁", url=f"https://t.me/MR_X_N"),
                ],
                [
                    InlineKeyboardButton(
                    "𓂄𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝙼𝚁_𝚇𓆪𓂁", url=f"https://t.me/MR_X_N"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["المطور","مطور","المستر","مستر"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/08d12aa31c5c41e51f6f2.jpg",
        caption=f""" 𝘞𝘌𝘓𝘊𝘖𝘔𝘌 𝘝𝘌𝘕𝘖𝘔 """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𓂄𓆩𝙾𝚂𝙰𝙼𝙰 𝚅𝙴𝙽𝙾𝙼𓆪𓂁", url=f"https://t.me/WWWL5"),
           ],
            [ 
                InlineKeyboardButton(
                    "𓂄𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝚅𝙴𝙽𝙾𝙼𓆪𓂁", url=f"https://t.me/MRv7x"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["سورس","ياسورس","السورس","source","يا سورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/08d12aa31c5c41e51f6f2.jpg",
        caption=f"""[⊱⋅━═━═『 𝗩𝗘𝗡𝗢𝗠 』═━═━⋅⊰](https://t.me/MRv7x)

 [● قـنـاة الـسـورس 🎧](https://t.me/MRv7x)
 [● مـبـرمـج الـسـورس 👨‍✈️](https://t.me/WWWL5)
 [● مـطـوريـن السورس 👨‍💻](https://t.me/SOURCE_VENOM)
 [● تنصيب بوتك حماية ⚡](https://t.me/G1VENOMbot)
 [● تنصيب بوتك ميوزك 🎧](https://t.me/WWWL5)

[⊱⋅━═━═『 𝗩𝗘𝗡𝗢𝗠 』═━═━⋅⊰](https://t.me/MRv7x)""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𝘀𝗼𝗨𝗥𝗰𝗲 𝘃𝗲𝗡𝗼𝗺", url=f"https://t.me/MRv7x"),
            ],
            [
            InlineKeyboardButton("𝗼𝘀𝗔𝗺𝗔 𝘃𝗲𝗡𝗼𝗺", url=f"https://t.me/WWWL5"),
            ],
            [
                InlineKeyboardButton(
                        "𝗗𝗲𝘃𝗲𝗟𝗼𝗣𝗲𝗥𝘀", url=f"https://t.me/SOURCE_VENOM"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                " **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                " **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🌐 ¦ الـقـنـاة ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            ],
                            [
                            InlineKeyboardButton("🎧 ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "أضف لبوت لمجموعتك ✅", url=f'https://t.me/{bu}?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
