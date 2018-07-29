from collections import namedtuple

# mapping saving amounts to a score
saving_score = namedtuple("saving_to_score", ["saving_amount", "score"])
l_saving_score = (
    saving_score(0, 1),
    saving_score(2000, 2),
    saving_score(4000, 3),
    saving_score(6000, 4),
    saving_score(8000, 5),
    saving_score(10000, 6)
)  
accepted_saving_amounts = [el.saving_amount for el in l_saving_score]

# mapping loan amounts to a score
loan_score = namedtuple("loan_to_score", ["loan_amount", "score"])
l_loan_score = (
    loan_score(0, 6),
    loan_score(2000, 5),
    loan_score(4000, 4),
    loan_score(6000, 3),
    loan_score(8000, 2),
    loan_score(10000, 1)
)  
accepted_loan_amounts = [el.loan_amount for el in l_loan_score]

# mapping total score to profile rank
predicate_rank = namedtuple("loan_to_score", ["predicate", "profile_rank"])
l_predicate_rank = (
    predicate_rank(lambda score : score >= 8, "A"),
    predicate_rank(lambda score : score >= 6, "B"),
    predicate_rank(lambda score : score >= 4, "C"),
    predicate_rank(lambda score : score >= 2, "D")
)

def get_score_from_saving_amount(saving_amount):
    assert saving_amount in accepted_saving_amounts
    return [el.score for el in l_saving_score if el.saving_amount == saving_amount][0]

def get_score_from_loan_amount(loan_amount):
    assert loan_amount in accepted_loan_amounts
    return [el.score for el in l_loan_score if el.loan_amount == loan_amount][0]

def get_user_profile(saving_amount, loan_amount):
    score = get_score_from_saving_amount(saving_amount) + get_score_from_loan_amount(loan_amount)
    return [el.profile_rank for el in l_predicate_rank if el.predicate(score)][0]


if __name__ == "__main__":
    profile = get_user_profile(2000, 2000)
    print(profile)