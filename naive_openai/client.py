import random
import time
from openai import OpenAI
from openai.resources import Chat
from openai.resources.chat import Completions

class NaiveOpenAI(OpenAI):
    def __init__(self, *args, degradation_rate=0, **kwargs):
        super().__init__(*args, **kwargs)
        if degradation_rate < 0 or degradation_rate > 1:
            raise ValueError("degradation_rate should be between 0 and 1")
        self.degradation_rate = degradation_rate
        self.chat = self.NaiveChat(self, degradation_rate=self.degradation_rate)

    class NaiveChat(Chat):
        def __init__(self, client, degradation_rate=0):
            super().__init__(client)
            self.degradation_rate = degradation_rate
            self.completions = self.NaiveCompletions(client, degradation_rate=degradation_rate)

        class NaiveCompletions(Completions):
            def __init__(self, client, degradation_rate=0):
                super().__init__(client)
                self.degradation_rate = degradation_rate

            def create(self, *args, **kwargs):
                start_time = time.time()
                # Degrade the model with the probability of degradation_rate
                if "model" in kwargs:
                    if random.random() < self.degradation_rate:
                        kwargs["model"] = "gpt-3.5-turbo"
                result = super().create(*args, **kwargs)
                elapsed_time = time.time() - start_time
                # Degrade the response time
                time.sleep(elapsed_time * self.degradation_rate)
                return result
