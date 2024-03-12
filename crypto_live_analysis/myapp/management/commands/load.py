async def load_from_json(filename):
    async with aiofiles.open(filename, 'r') as file:
        return json.loads(await file.read())