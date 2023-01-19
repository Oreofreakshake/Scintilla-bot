from cogs.events.memberjoin import memberjoin
from cogs.events.memberleft import memberleft


class Commands:
    def __init__(self, bot):
        self.bot = bot

    async def memberjoin(self, message):
        await memberjoin(self.bot, message)

    async def memberleft(self, message):
        await memberleft(self.bot, message)


print("Events successfully initialized!\n")
