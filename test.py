import asyncio

from smsaero.client import SMSAero

a = SMSAero(
    email="",
    api_key="",
)


async def main():
    print(await a.flash_call.send(phone=79554443322, code="0000"))
    # print(await a.flash_call.get_one(_id=1710585))
    # print(await a.flash_call.get_all())
    # data = await a.balance.get()
    # print(data.data.balance)


asyncio.run(main())
