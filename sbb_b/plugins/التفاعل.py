import emoji
from telethon.tl.functions.messages import SendReactionRequest
from email import message
from sbb_b import sbb_b

EMOJI = ["👍", "👎", "❤️", "🔥", "👏", "😁", "🤬", "🤩", "🤮", "💩", "🙏"]

@sbb_b.ar_cmd(pattern="تفاعل (.*)")
async def reaction(event):
    reply = await event.get_reply_message()
    jmthon = event.pattern_match.group(1)
    if jmthon not in EMOJI:
        await event.edit("**• لقد وضعت تعبير غير صحيح او غير متاح**\n\n**يجب عليك استخدام احد التعابير التالية فقط:** `👍` `👎` `❤️` `🔥` `👏` `😁` `🤬` `🤩` `🤮` `💩` `🙏`")
        return
    if not reply:
        await event.edit("**• عليك الرد على الرسالة للتفاعل معها اولا**\n\n**الأستخدام:** `.تفاعل` `👍` `👎` `❤️` `🔥` `👏` `😁` `🤬` `🤩` `🤮` `💩` `🙏`")
        return
    elif "👍" == jmthon:
        jmthon = emoji.emojize(':thumbs_up:')
    elif "👎" == jmthon:
        jmthon = emoji.emojize(':thumbs_down:')
    elif "❤️" == jmthon:
        jmthon = emoji.emojize(':red_heart:')
    elif "🔥" == jmthon:
        jmthon = emoji.emojize(':fire:')
    elif "👏" == jmthon:
        jmthon = emoji.emojize(':clapping_hands:')
    elif "😁" == jmthon:
        jmthon = emoji.emojize(':beaming_face_with_smiling_eyes:')
    elif "🤬" == jmthon:
        jmthon = emoji.emojize(':face_with_symbols_on_mouth:')
    elif "🤩" == jmthon:
        jmthon = emoji.emojize(':star-struck:')
    elif "🤮" == jmthon:
        jmthon = emoji.emojize(':face_vomiting:')
    elif "💩" == jmthon:
        jmthon = emoji.emojize(':pile_of_poo:')
    elif "🙏" == jmthon:
        jmthon = emoji.emojize(':folded_hands:')
    elif "🥱" == jmthon:
        jmthon = emoji.emojize(':yawning_face:')
    elif "🥴" == jmthon:
        jmthon = emoji.emojize(':woozy_face:')
    try: 
        message_id = reply.id
        await event.delete()   
        await sbb_b(SendReactionRequest(peer=event.chat_id, msg_id=message_id, reaction=jmthon))
    except Exception as e:
        await event.edit(e)
