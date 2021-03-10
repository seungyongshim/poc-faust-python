from typing import AsyncIterable
from faust import StreamT
import faust


class Add(faust.Record):
    a: int
    b: int


app = faust.App("simple_rpc", reply_create_topic=True)

topic = app.topic(
    "adding",
    value_type=Add,
)


@app.agent(topic)
async def adding(stream: StreamT[Add]) -> AsyncIterable[int]:
    async for value in stream:
        yield value.a + value.b
