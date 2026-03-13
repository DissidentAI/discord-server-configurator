class ConfigValidation:
    def __init__(self, config):
        self.config = config

    def validate(self):
        # Add validation logic here
        pass

    def get_errors(self):
        # Method to return validation errors
        return []


class DatabaseConfig(ConfigValidation):
    def validate(self):
        super().validate()
        # Add database specific validation logic
        pass


class APIConfig(ConfigValidation):
    def validate(self):
        super().validate()
        # Add API specific validation logic
        pass
