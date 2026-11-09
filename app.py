
import streamlit as st

# -----------------------------------------
# 1. Set up the webpage
# -----------------------------------------

st.set_page_config(
    page_title="Tip Calculator",
    page_icon="💵",
    layout="centered"
)

# -----------------------------------------
# 2. Display the title and description
# -----------------------------------------

st.title("💵 Restaurant Tip Calculator")

st.write(
    "Calculate your restaurant tip and find out "
    "how much each person owes."
)

st.divider()

# -----------------------------------------
# 3. Allow users to enter the bill amount
# -----------------------------------------

bill_amount = st.number_input(
    "Enter the restaurant bill ($):",
    min_value=0.0,
    value=50.00,
    step=1.00
)

# -----------------------------------------
# 4. Allow users to select a tip percentage
# -----------------------------------------

tip_percentage = st.selectbox(
    "Select your tip percentage:",
    [10, 15, 18, 20, 25]
)

# -----------------------------------------
# 5. Allow users to enter the number of people
# -----------------------------------------

people = st.number_input(
    "How many people are splitting the bill?",
    min_value=1,
    value=2,
    step=1
)

# -----------------------------------------
# 6. Calculate the tip and total bill
# -----------------------------------------

if st.button("Calculate Tip", type="primary"):

    # Convert the tip percentage into a decimal
    tip_rate = tip_percentage / 100

    # Calculate the tip amount
    tip_amount = bill_amount * tip_rate

    # Calculate the total bill including tip
    total_bill = bill_amount + tip_amount

    # Calculate each person's share
    amount_per_person = total_bill / people

    # -----------------------------------------
    # 7. Display the results
    # -----------------------------------------

    st.success("Your tip calculation is complete!")

    st.subheader("Your Results")

    st.metric(
        "Tip Amount",
        f"${tip_amount:,.2f}"
    )

    st.metric(
        "Total Bill Including Tip",
        f"${total_bill:,.2f}"
    )

    st.metric(
        "Amount Per Person",
        f"${amount_per_person:,.2f}"
    )

    # -----------------------------------------
    # 8. Display the formulas used
    # -----------------------------------------

    st.subheader("Formulas Used")

    st.write("**Tip Amount:**")

    st.latex(
        r"\text{Bill Amount} \times \text{Tip Percentage}"
    )

    st.write("**Total Bill:**")

    st.latex(
        r"\text{Bill Amount} + \text{Tip Amount}"
    )

    st.write("**Amount Per Person:**")

    st.latex(
        r"\frac{\text{Total Bill}}{\text{Number of People}}"
    )

    # -----------------------------------------
    # 9. Display a calculation summary
    # -----------------------------------------

    st.subheader("Calculation Summary")

    st.write(f"Original Bill: ${bill_amount:,.2f}")
    st.write(f"Tip Percentage: {tip_percentage}%")
    st.write(f"Tip Amount: ${tip_amount:,.2f}")
    st.write(f"Number of People: {people}")
    st.write(f"Total Bill: ${total_bill:,.2f}")

# -----------------------------------------
# 10. Add a footer
# -----------------------------------------

st.divider()

st.caption("Restaurant Tip Calculator | Built with Python and Streamlit")
