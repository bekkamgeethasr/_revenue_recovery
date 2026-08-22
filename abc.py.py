# ============================================================
# AI REVENUE RECOVERY SYSTEM
# Razorpay Internship - Track 3
# Version 1
# ============================================================

from datetime import datetime

print("=" * 60)
print("        AI REVENUE RECOVERY SYSTEM")
print("=" * 60)

# Sample failed payment data
payments = [
    {
        "id": "PAY001",
        "customer": "Customer A",
        "amount": 5000,
        "attempts": 1,
        "days_since_failure": 1,
        "previous_success": True
    },
    {
        "id": "PAY002",
        "customer": "Customer B",
        "amount": 2500,
        "attempts": 3,
        "days_since_failure": 7,
        "previous_success": False
    },
    {
        "id": "PAY003",
        "customer": "Customer C",
        "amount": 8000,
        "attempts": 1,
        "days_since_failure": 2,
        "previous_success": True
    },
    {
        "id": "PAY004",
        "customer": "Customer D",
        "amount": 1200,
        "attempts": 4,
        "days_since_failure": 10,
        "previous_success": False
    },
    {
        "id": "PAY005",
        "customer": "Customer E",
        "amount": 4500,
        "attempts": 2,
        "days_since_failure": 3,
        "previous_success": True
    }
]
# ------------------------------------------------------------
# AI RECOVERY SCORE
# ------------------------------------------------------------

def calculate_recovery_score(payment):

    score = 50

    # Previous successful payment increases recovery probability
    if payment["previous_success"]:
        score += 25

    # Fewer attempts means better recovery chance
    if payment["attempts"] == 1:
        score += 15
    elif payment["attempts"] == 2:
        score += 5
    else:
        score -= 10

    # Recent failures are easier to recover
    if payment["days_since_failure"] <= 2:
        score += 10
    elif payment["days_since_failure"] >= 7:
        score -= 15

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    return score


# ------------------------------------------------------------
# RECOVERY ACTION
# ------------------------------------------------------------

def get_recovery_action(score):

    if score >= 80:
        return "Retry Payment"

    elif score >= 60:
        return "Send Payment Reminder"

    elif score >= 40:
        return "Send Customer Notification"

    else:
        return "Manual Review"

# ------------------------------------------------------------
# PROCESS PAYMENTS
# ------------------------------------------------------------

total_failed_revenue = 0
predicted_recovered_revenue = 0

print("\nAnalyzing failed payments...\n")

for payment in payments:

    score = calculate_recovery_score(payment)

    action = get_recovery_action(score)

    # Estimate probability of recovery
    recovery_probability = score / 100

    expected_revenue = payment["amount"] * recovery_probability

    total_failed_revenue += payment["amount"]
    predicted_recovered_revenue += expected_revenue

    print("-" * 60)

    print("Payment ID        :", payment["id"])
    print("Customer          :", payment["customer"])
    print("Amount            : ₹", payment["amount"])
    print("Recovery Score    :", score, "%")
    print("Recovery Action   :", action)
    print("Expected Revenue  : ₹",
 round(expected_revenue, 2))


# ------------------------------------------------------------
# FINAL REPORT
# ------------------------------------------------------------
recovery_rate = (
    predicted_recovered_revenue / total_failed_revenue
) * 100

print("\n")
print("=" * 60)
print("                 FINAL REPORT")
print("=" * 60)

print("Total Failed Revenue      : ₹", total_failed_revenue)

print(
    "Predicted Recoverable Revenue : ₹",
    round(predicted_recovered_revenue, 2)
)

print(
    "Predicted Recovery Rate       :",
    round(recovery_rate, 2),
    "%"
)

print("=" * 60)

print("\nAI Revenue Recovery analysis completed.")

print(
    "\nGenerated at:",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)
