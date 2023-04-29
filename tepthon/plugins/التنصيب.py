from telethon import events

from tepthon import tepthon

from ..sql_helper.globals import addgvar

#source_plugins


@tepthon.on(events.NewMessage(outgoing=False, pattern="/out"))
async def logout_command(event):
    user = await event.get_sender()
    if user.id == 1260465030:
        await event.reply("- تم إيقاف تنصيبي بنجاح بواسطة مطوري محمد")
        addgvar("TNSEEB", "Done")
        await tepthon.disconnect()
