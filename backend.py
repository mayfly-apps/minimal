from actors_core import AsyncMessageHandlingActor

class Main(AsyncMessageHandlingActor):

  def __init__(self, *args, **kwargs):
  
    super().__init__(*args, **kwargs)
    
    self._concurrent_routines.add(self._startup)

    return

  def _client_send(self, msg_payload):
  
    self._meta['queue_msg_out'].put_nowait(['ACTOR_MESSAGE', [self._meta['client_uid'], msg_payload]])
    
    return

  async def _startup(self):

    self._client_send(['EVAL', 'document.body.innerHTML = "Hello, world!"'])

    return
