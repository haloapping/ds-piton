class Profile:
    def __init__(self, name: str, social_media: dict[str, str], website: str):
        self.name: str = name
        self.social_media: dict[str, str] = social_media
        self.website: str = website

    def __str__(self) -> str:
        return (
            f"Name         : {self.name}\n"
            f"Social Media : {self.social_media}\n"
            f"Website      : {self.website}\n"
            f":-)"
        )


profile = Profile(
    "Apping",
    {"twitter": "haloapping", "instagram": "haloapping", "github": "haloapping"},
    "haloapping.github.io",
)

print(profile)
