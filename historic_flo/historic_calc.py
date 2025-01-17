    """
    Add calculation to history and save log
    """

    # Add the calculation to the history
    history.append({
        'num1': num1,
        'operation': operator,
        'num2': num2,
        'result': result
    })

    save_history_log(history)