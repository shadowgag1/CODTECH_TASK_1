import re


common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567",
    "1234567890", "qwerty", "abc123", "111111", "password1", "iloveyou"
]


def check_length(password):
    length = len(password)
    if length < 6:
        return "Very Weak", 1
    elif length < 8:
        return "Weak", 2
    elif length < 12:
        return "Moderate", 3
    else:
        return "Strong", 4


def check_complexity(password):
    score = 0
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        
    complexity = ["Very Weak", "Weak", "Moderate", "Strong"]
    return complexity[score-1], score


def check_uniqueness(password):
    if password in common_passwords:
        return "Very Weak", 1
    else:
        return "Strong", 4

def assess_password_strength(password):
    length_rating, length_score = check_length(password)
    complexity_rating, complexity_score = check_complexity(password)
    uniqueness_rating, uniqueness_score = check_uniqueness(password)

    total_score = length_score + complexity_score + uniqueness_score
    average_score = total_score / 3
    
    strength = ["Very Weak", "Weak", "Moderate", "Strong"]
    
    overall_strength = strength[int(average_score) - 1]
    
    return {
        "length": length_rating,
        "complexity": complexity_rating,
        "uniqueness": uniqueness_rating,
        "overall": overall_strength
    }


def provide_feedback(assessment):
    feedback = []
    if assessment["length"] in ["Very Weak", "Weak"]:
        feedback.append("Consider making your password longer.")
    if assessment["complexity"] in ["Very Weak", "Weak"]:
        feedback.append("Add a mix of upper and lower case letters, numbers, and special characters.")
    if assessment["uniqueness"] == "Very Weak":
        feedback.append("Avoid common passwords or patterns.")
    
    return feedback


password = "P@ssw0rd123!"
strength = assess_password_strength(password)
print("Password Strength Assessment:")
print(strength)

feedback = provide_feedback(strength)
print("\nFeedback:")
for tip in feedback:
    print(tip)
