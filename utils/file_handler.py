from __future__ import annotations

import json

import aiofiles


async def load_json(filepath):
    """Load data from a json file."""
    async with aiofiles.open(filepath, 'r') as file:
        content = await file.read()
        return json.loads(content)


async def save_json(data, filename):
    """Save data to a json file."""
    async with aiofiles.open(filename, 'w') as file:
        await file.write(json.dumps(data))


async def amend_json(data, filename):
    """Amend a json file with new data."""
    async with aiofiles.open(filename, 'r') as file:
        content = await file.read()
        existing_data = json.loads(content)
        existing_data.append(data)

    async with aiofiles.open(filename, 'w') as file:
        await file.write(json.dumps(existing_data))
