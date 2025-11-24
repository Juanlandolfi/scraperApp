class BasePipeline:
    async def process_item(self, item: dict):
        raise NotImplementedError