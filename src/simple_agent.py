from typing import AsyncIterable
from faust import StreamT
import faust


class Add(faust.Record):
    a: int
    b: int


app = faust.App("simple_rpc")


topic = app.topic(
    "adding",
    value_type=Add,
)


@app.agent(app.topic("topic"))
async def mytask(events):
    async for event in events:
        print(app.monitor.events_s)


@app.agent(topic)
async def adding(stream: StreamT[Add]) -> AsyncIterable[int]:
    async for value in stream:
        yield value.a + value.b
