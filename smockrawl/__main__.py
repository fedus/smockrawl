import asyncio
import aiohttp

from smockrawl.smockrawl import Smockeo


async def main():
    print("smockrawl - Smockeo crawler - CLI example")
    username = input("Smockeo username: ")
    password = input("Smockeo password: ")
    detectorId = input("Smockeo detector ID: ")

    async with aiohttp.ClientSession() as session:
        smo = Smockeo(username, password, detectorId, loop, session)

        await smo.authenticate()
        await smo.poll()

        smo.print_status()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
