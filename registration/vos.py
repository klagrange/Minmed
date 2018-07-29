def access_vo(access):
    return {
        "token": access.token
    }

def user_vo(user):
    user_vo = {
        "username": user.username,
        "password": user.password,
        "savingAmount": user.saving_amount,
        "loanAmount": user.loan_amount,
    }
    return user_vo
