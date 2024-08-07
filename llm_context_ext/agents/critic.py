from llm_context_ext.agents import LLMAgent
from llm_context_ext.helpers.file import read_system_message, read_user_message

class Critic(LLMAgent):
    user_message_template: str

    def __init__(self):
        super().__init__(read_system_message(self))
        self.user_message_template = read_user_message(self)

    def chat(self, first_user_message: str, context: str):
        user_message = self.user_message_template.format(first_user_message=first_user_message, context=context)

        self.messages.append(
            {
                "role": "user", 
                "content": user_message
            }
        )

        response = super().generate()

        return response
        


if __name__ == "__main__":
    critic = Critic()

    print(critic.system_message)
    print("==========================================")
    print(assistant.user_message)