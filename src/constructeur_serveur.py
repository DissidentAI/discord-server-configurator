class DiscordServerBuilder:
    def __init__(self):
        self.server_name = ""
        self.channels = []
        self.roles = []

    def set_server_name(self, name):
        self.server_name = name

    def add_channel(self, channel_name):
        self.channels.append(channel_name)

    def add_role(self, role_name):
        self.roles.append(role_name)

    def build(self):
        return {
            'server_name': self.server_name,
            'channels': self.channels,
            'roles': self.roles
        }

# Example usage:
# builder = DiscordServerBuilder()
# builder.set_server_name("My Cool Server")
# builder.add_channel("general")
# builder.add_role("admin")
# server_config = builder.build()
# print(server_config)