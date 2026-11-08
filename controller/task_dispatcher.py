def dispatch(agent, task):
    # Chỉ truyền input; expected_output không bao giờ gửi đến model.
    return agent.respond(task.input)
