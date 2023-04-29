from os import remove

from tepthon import tepthon


@tepthon.ar_cmd(pattern="(سي|ذاتية)")
async def datea(event):
    await event.delete()
    scertpic = await event.get_reply_message()
    downloadjmthon = await scertpic.download_media()
    await tepthon.send_file("me", downloadjmthon)
    remove(downloadjmthon)
