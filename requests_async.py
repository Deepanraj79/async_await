import aiohttp
import asyncio
import time

start_time = time.time()


async def main():

    async with aiohttp.ClientSession() as session:

        for number in range(1, 5):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])

asyncio.get_event_loop().run_until_complete(main())  # asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))