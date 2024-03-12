from django.core.management.base import BaseCommand
from pipe import load_from_json
async def load_from_json(filename):
    async with aiofiles.open(filename, 'r') as file:
        return json.loads(await file.read())
    
class Command(BaseCommand):
    help = 'Describe command'
    
    data = await load_from_json('data/tests/fetch_ticker_1.json')

    def handle(self, *args, **kwargs):
        # Data processing logic
        print(data)
        self.stdout.write(self.style.SUCCESS('Successfully ran data processing pipeline'))
