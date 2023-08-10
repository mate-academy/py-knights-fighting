def results(members: dict) -> dict:
    return {member.name: member.hp for member in members.values()}
